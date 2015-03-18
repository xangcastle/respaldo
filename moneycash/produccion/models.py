from django.db import models
from moneycash.entidad import Entidad, datos_generales
from moneycash.documento import Documento
from django.contrib.auth.models import User
from moneycash.models import Periodo as base_periodo
from django.db.models import Sum


def activar_equipos(periodo):
    es = Equipo.objects.filter(activo=True)
    for e in es:
        n = equipo_periodo(periodo=periodo, equipo=e,
            contador_inicial=e.contador_actual,
            contador_final=e.contador_actual)
        n.save()


def crear_recibos(periodo):
    areas = Area.objects.filter(activo=True).values_list('id', flat=True)
    recibos = Recibo.objects.filter(periodo=periodo)
    if recibos:
        areas = list(set(areas) - set(recibos.values_list('area_id',
            flat=True)))
    for a in areas:
        area = Area.objects.get(id=a)
        r = Recibo(fecha=periodo.fin_produccion, area=area)
        r.save()
        for e in area.equipos.all():
            rd = recibo_detalle(recibo=r, equipo=e, precio=e.precio_copia,
                fecha_inicial=periodo.inicio_produccion,
                fecha_final=periodo.fin_produccion)
            rd.save()


def cargar_copias(periodo):
    equipos = equipo_periodo.objects.filter(periodo=periodo)
    recibos = Recibo.objects.filter(periodo=periodo)
    for e in equipos:
        areas = recibo_detalle.objects.filter(equipo=e.equipo,
            recibo__in=recibos)
        total = areas.count()
        copias = 0
        if total > 0:
            copias = round(e.copias / total, 0)
        areas.update(copias=copias)
    for r in recibos:
        r.calcular()
        r.save()


class Periodo(base_periodo):
    class Meta:
        proxy = True

    def equipos(self):
        return equipo_periodo.objects.filter(periodo=self)

    def recibos(self):
        return Recibo.objects.filter(periodo=self)

    def copias_equipos(self):
        if self.equipos():
            return self.equipos().aggregate(Sum('copias'))['copias__sum']

    def copias_areas(self):
        if self.equipos():
            return self.recibos().aggregate(Sum('copias'))['copias__sum']


class equipo_periodo(models.Model):
    periodo = models.ForeignKey(Periodo)
    equipo = models.ForeignKey('Equipo')
    contador_inicial = models.PositiveIntegerField()
    contador_final = models.PositiveIntegerField()
    copias = models.PositiveIntegerField(null=True, blank=True, default=0)

    #def __unicode__(self):
        #return str(self.equipo) + str(self.total_copias)

    def get_copias(self):
        if self.contador_inicial and self.contador_final:
            return self.contador_final - self.contador_inicial
        else:
            return 0

    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos en produccion'

    def save(self, *args, **kwargs):
        self.copias = self.get_copias()
        self.equipo.actualizar_contador(self.contador_final)
        super(equipo_periodo, self).save()


class recibo_detalle(models.Model):
    recibo = models.ForeignKey('Recibo')
    equipo = models.ForeignKey('Equipo')
    copias = models.FloatField(default=0.0)
    precio = models.FloatField(default=0.0)
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()

    def __unicode__(self):
        return str(self.equipo) + ' copias: ' + str(self.copias)

    def importe(self):
        return round(self.copias * self.precio, 2)

    def dias_facturados(self):
        return int((self.fecha_final - self.fecha_inicial).days)

    def top(self):
        top = 0
        for r in recibo_detalle.objects.filter(
            recibo=self.recibo).order_by('equipo'):
                if r.id == self.id:
                    return 363 + (top * 20)
                top += 1

    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'detalle de copias por equipo'

    def save(self, *args, **kwargs):
        super(recibo_detalle, self).save()
        self.recibo.save()


class Recibo(Documento):
    area = models.ForeignKey('Area')
    copias = models.FloatField(default=0.0)
    importe = models.FloatField(default=0.0)
    tc = models.FloatField(default=0.0)

    def detalle(self):
        return recibo_detalle.objects.filter(recibo=self)

    def get_copias(self):
        copias = 0
        if self.detalle():
            copias += self.detalle().aggregate(Sum('copias'))['copias__sum']
        return copias

    def get_importe(self):
        monto = 0.0
        if self.detalle():
            for d in self.detalle():
                monto += d.importe()
        return round(monto, 2)

    def calcular(self):
        self.copias = self.get_copias()
        self.importe = self.get_importe()

    def str_numero(self):
        if self.numero:
            return str(self.numero).zfill(6)
        else:
            return '0'.zfill(6)

    def ultimos_seis(self):
        ps = Periodo.objects.filter(
            fecha_inicial__lte=self.periodo.fecha_inicial)[:10]
        rs = Recibo.objects.filter(periodo__in=ps,
            area=self.area).order_by('fecha')
        data = []
        for r in rs:
            d = {'periodo': str(r.periodo)[:3], 'copias': r.copias}
            data.append(d)
        return data

    def save(self, *args, **kwargs):
        self.calcular()
        super(Recibo, self).save()


class Area(Entidad):
    cliente = models.ForeignKey('Cliente')
    ubicacion = models.ForeignKey('Ubicacion')
    encargado = models.CharField(max_length=100, default='')
    unidad_ejecutora = models.CharField(max_length=10, default='')
    equipos = models.ManyToManyField('Equipo',
        verbose_name='equipos que usa el area')


class Ubicacion(Entidad):
    user = models.ForeignKey(User)
    direccion = models.TextField(max_length=250, null=True, blank=True)


class Cliente(Entidad, datos_generales):
    pass


class Equipo(Entidad):
    marca = models.ForeignKey('Marca')
    modelo = models.CharField(max_length=30, default='')
    serie = models.CharField(max_length=30, default='')

    ubicacion = models.ForeignKey('Ubicacion', null=True, blank=True)
    velocidad = models.PositiveIntegerField(default=0,
        verbose_name='velocidad del equipo')
    precio_copia = models.FloatField(null=True, blank=True)
    costo_copia = models.FloatField(null=True, blank=True)

    contador_inicial = models.PositiveIntegerField(default=0,
        help_text='contador que tenia el equipo al momento de la compra')
    contador_actual = models.PositiveIntegerField(default=0)
    vida_util = models.PositiveIntegerField(default=1000000)
    costo_compra = models.FloatField(null=True, blank=True,
        verbose_name='costo de compra')
    depreciacion_copia = models.FloatField(null=True, blank=True,
        verbose_name='depreciacion por copia')
    valor_depreciado = models.FloatField(null=True, blank=True,
        verbose_name='total depreciado')
    precio_venta = models.FloatField(null=True, blank=True,
        verbose_name='valor en libros')

    def __unicode__(self):
        s = []
        if self.code:
            s.append(self.code)
        if self.modelo:
            s.append(self.modelo)
        if self.serie:
            s.append(self.serie)
        return ' - '.join(s)

    def actualizar_contador(self, c):
        if c > self.contador_actual:
            self.contador_actual = c

    def depreciar(self):
        if self.contador_inicial and self.contador_actual and self.vida_util \
            and self.costo_compra \
            and self.contador_actual > self.contador_inicial:
            self.depreciacion_copia = round(self.costo_compra / (
                self.vida_util - self.contador_inicial), 4)
            self.valor_depreciado = round(self.depreciacion_copia * (
                self.contador_actual - self.contador_inicial), 2)
            self.precio_venta = round(self.costo_compra
            - self.valor_depreciado, 2)

    def save(self, *args, **kwargs):
        self.depreciar()
        super(Equipo, self).save()


class Marca(Entidad):
    pass