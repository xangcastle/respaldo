# -*- coding: latin-1 -*-
from django.db import models
from django.db.models import Max
import os
from django.conf import settings
from django.contrib.auth.models import User


def get_code(entidad):
        model = type(entidad)
        code = ''
        sets = model.objects.all()
        if sets:
            maxi = str(sets.aggregate(Max('code'))['code__max'])
            if maxi:
                consecutivo = list(range(1, int(maxi)))
                ocupados = list(sets.values_list('code',
                flat=True))
                n = 0
                for l in ocupados:
                    ocupados[n] = int(str(l))
                    n += 1
                disponibles = list(set(consecutivo) - set(ocupados))
                if len(disponibles) > 0:
                    code = min(disponibles)
                else:
                    code = max(ocupados) + 1
        return str(code).zfill(4)


def get_media_url(model, filename):
    clase = model.__class__.__name__
    code = str(model.id)
    return '%s/%s/%s' % (clase, code, filename)


def get_ruta(paquete):
    carpata_madre = str(paquete.ano)[2:4] + str(paquete.mes).zfill(2) \
        + str(paquete.ciclo).zfill(2)
    carpeta_ciclo = ''
    if paquete.ciclo in (33, 88):
        carpeta_ciclo = 'internet'
    if paquete.ciclo in (55, 66):
        carpeta_ciclo = 'lineas_fijas'
    if paquete.ciclo in (65, 51):
        carpeta_ciclo = 'lineas_moviles'
    if paquete.ciclo in (10,):
        carpeta_ciclo = 'datos'
    if paquete.ciclo in (1, 77, 11, 76):
        carpeta_ciclo = 'TV'
    ruta = os.path.join('POD', carpata_madre, 'Factura PDF',
        carpeta_ciclo)
    return ruta


def generar_ruta_comprobante(paquete, filename):
        extension = os.path.splitext(filename)[1][1:]
        nombre = str(paquete.contrato) + str(paquete.ciclo) \
         + str(paquete.mes).zfill(2) + str(paquete.ano)[2:4]
        nombre_archivo = '{}.{}'.format(nombre, extension)
        return os.path.join(get_ruta(paquete), nombre_archivo)


class base(models.Model):

    def __iter__(self):
        for field_name in self._meta.get_all_field_names():
            try:
                value = getattr(self, field_name)
            except:
                value = None
            yield (field_name, value)

    class Meta:
        abstract = True


class base_entidad(base):
    code = models.CharField(max_length=25, null=True, blank=True,
        verbose_name="codigo")
    name = models.CharField(max_length=100, verbose_name="nombre")

    class Meta:
        abstract = True


class Entidad(base_entidad):
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        if self.code and self.name:
            return str(self.code) + " " + self.name
        elif self.name:
            return self.name
        elif self.code:
            return str(self.code)
        else:
            return ''

    def save(self, *args, **kwargs):
        if self.code is None or self.code == '':
            self.code = get_code(self)
        super(Entidad, self).save()

    class Meta:
        abstract = True
        ordering = ['code']


class Paquete(base):
    archivo = models.CharField(max_length=100, null=True, blank=True)
    consecutivo = models.PositiveIntegerField(null=True, blank=True)
    contrato = models.PositiveIntegerField(null=True, blank=True)
    factura = models.CharField(max_length=70, null=True, blank=True)
    ciclo = models.PositiveIntegerField(null=True, blank=True)
    mes = models.PositiveIntegerField(null=True, blank=True)
    ano = models.PositiveIntegerField(null=True, blank=True)
    cliente = models.CharField(max_length=150, null=True, blank=True)
    direccion = models.TextField(max_length=250, null=True, blank=True)
    barrio = models.CharField(max_length=150, null=True, blank=True)
    municipio = models.CharField(max_length=150, null=True, blank=True)
    departamento = models.CharField(max_length=150, null=True, blank=True)
    distribuidor = models.CharField(max_length=150, null=True, blank=True)
    ruta = models.CharField(max_length=25, null=True, blank=True)
    zona = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    segmento = models.CharField(max_length=50, null=True, blank=True)
    tarifa = models.CharField(max_length=70, null=True, blank=True)
    idbarrio = models.PositiveIntegerField(null=True, blank=True)
    iddepartemento = models.PositiveIntegerField(null=True, blank=True)
    idmunicipio = models.PositiveIntegerField(null=True, blank=True)
    servicio = models.CharField(max_length=70, null=True, blank=True)
    cupon = models.PositiveIntegerField(null=True, blank=True)
    total_mes_factura = models.FloatField(null=True, blank=True)
    valor_pagar = models.FloatField(null=True, blank=True)
    entrega = models.BooleanField(default=False, verbose_name='entregada')
    numero_fiscal = models.PositiveIntegerField(null=True, blank=True)
    factura_interna = models.PositiveIntegerField(null=True, blank=True)
    telefono_contacto = models.CharField(max_length=70, null=True, blank=True)
    ESTADOS = (('PE', 'PENDIENTE'), ('EN', 'ENTREGADO'), ('AS', 'ASIGNADO'))
    estado = models.CharField(max_length=2, choices=ESTADOS, default='PE')
    colector = models.ForeignKey('Colector', null=True, blank=True)
    lote = models.ForeignKey('Lote', null=True, blank=True,
        on_delete=models.SET_NULL)
    lotificado = models.BooleanField(default=False)
    cerrado = models.BooleanField(default=False)
    comprobante = models.FileField(upload_to=get_media_url, null=True,
        blank=True)
    pod = models.FileField(upload_to=generar_ruta_comprobante, null=True,
        blank=True)
    barra = models.CharField(max_length=30, null=True, blank=True)

    orden_impresion = models.PositiveIntegerField(null=True, blank=True)

    def get_telefono(self):
        telefonos = []
        if self.telefono:
            telefonos.append(self.telefono)
        if self.telefono_contacto:
            telefonos.append(self.telefono_contacto)
        return ', '.join(telefonos)

    def link_comprobante(self):
        if self.pod:
            return '<a href="/media/%s" target="blank" onclick="return showAddAnotherPopup(this);">%s</a>' % (self.pod,
                'comprobante')
        if self.comprobante:
            return '<a href="/media/%s" target="blank" onclick="return showAddAnotherPopup(this);">%s</a>' % (self.comprobante,
                'comprobante')
        else:
            return None

    link_comprobante.short_description = 'comprobante'
    link_comprobante.allow_tags = True

    def __unicode__(self):
        return self.factura

    class Meta:
        verbose_name = 'factura'
        ordering = ['consecutivo']

    def integrar(self):
        try:
            d, created = Departamento.objects.get_or_create(
                id=self.iddepartemento, name=self.departamento)

            m, created = Municipio.objects.get_or_create(id=self.idmunicipio,
                name=self.municipio, departamento=d)

            b, created = Barrio.objects.get_or_create(id=self.idbarrio,
            name=self.barrio, municipio=m, departamento=d)

            c, created = Cliente.objects.get_or_create(name=self.cliente,
                contrato=self.contrato)
            c.contrato = self.contrato
            c.segmento = self.segmento
            c.tarifa = self.tarifa
            c.servicio = self.servicio
            c.telefono_contacto = self.telefono_contacto
            c.direccion = self.direccion
            c.distribuidor = self.distribuidor
            c.departamento = d
            c.municipio = m
            c.barrio = b
            c.valor_pagar = self.valor_pagar
            c.save()
        except:
            pass

    def get_lotificado(self):
        if self.lote:
            return True
        else:
            return False

    def get_entregado(self):
        if self.comprobante or self.pod:
            return True
        else:
            return False

    def get_barra(self):
        if self.contrato and self.ciclo and self.mes and self.ano:
            return str(self.contrato) + str(self.ciclo) \
            + str(self.mes).zfill(2) \
            + str(self.ano)
        else:
            return ''

    def get_colector(self):
        if self.entrega:
            pass
        else:
            if self.lote and self.lote.asignado():
                return self.lote.colector
            else:
                return None

    def save(self, *args, **kwargs):
        self.lotificado = self.get_lotificado()
        self.entrega = self.get_entregado()
        self.cerrado = False
        self.barra = self.get_barra()
        #self.colector = self.get_colector()
        super(Paquete, self).save()
        self.integrar()
        if self.lote:
            lote = Lote.objects.get(id=self.lote.id)
            lote.calcular()
            lote.save()


class Lote(base):
    fecha = models.DateTimeField(auto_now=True, null=True)
    numero = models.PositiveIntegerField()
    departamento = models.ForeignKey('Departamento', null=True, blank=True)
    municipio = models.ForeignKey('Municipio', null=True, blank=True)
    barrio = models.ForeignKey('Barrio', null=True, blank=True)
    colector = models.ForeignKey('Colector', null=True, blank=True)
    avance = models.CharField(max_length=10, null=True, blank=True,
        verbose_name='porcentaje de avance', default='0.00 %')
    cantidad_paquetes = models.PositiveIntegerField(null=True, blank=True,
    verbose_name='cantidad de facturas', default=0)
    entregados = models.PositiveIntegerField(null=True, blank=True,
        default=0, verbose_name='entregadas')
    cerrado = models.BooleanField(default=False)
    asignado = models.BooleanField(default=False)
    ciclo = models.PositiveIntegerField(null=True, blank=True)
    mes = models.PositiveIntegerField(null=True, blank=True)
    ano = models.PositiveIntegerField(null=True, blank=True)

    def get_numero(self):
        objs = Lote.objects.all()
        if objs:
            return objs.aggregate(Max('numero'))['numero__max'] + 1
        else:
            return 1

    def get_asignado(self):
        if self.colector:
            return True
        else:
            return False

    def paquetes(self):
        return Paquete.objects.filter(lote=self)

    def get_ciclo(self):
        if self.paquetes():
            return self.paquetes()[0].ciclo
        else:
            return None

    def get_mes(self):
        if self.paquetes():
            return self.paquetes()[0].mes
        else:
            return None

    def get_ano(self):
        if self.paquetes():
            return self.paquetes()[0].ano
        else:
            return None

    def calcular(self):
        if self.paquetes():
            self.cantidad_paquetes = int(self.paquetes().count())
            self.entregados = self.paquetes().filter(entrega=True).count()
            self.avance = str(((self.entregados * 100) /
            self.cantidad_paquetes)).zfill(3) \
            + ' %'

    def ordenar_por_direccion(self):
        ps = self.paquetes().order_by('direccion')
        position = 0
        for p in ps:
            p.consecutivo = position
            p.save()
            position += 1

    def ordenar_por_cliente(self):
        ps = self.paquetes().order_by('cliente')
        position = 0
        for p in ps:
            p.consecutivo = position
            p.save()
            position += 1

    def reasignar(self):
        pre = Lote.objects.get(id=self.id)
        if self.colector and pre.colector:
            if self.colector != pre.colector:
                self.paquetes().filter(entrega=False).update(
                    colector=self.colector)
        if not self.colector:
            self.paquetes().filter(entrega=False).update(colector=None)

    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = self.get_numero()
        self.asignado = self.get_asignado()
        self.reasignar()
        self.calcular()
        if self.cerrado:
            self.ciclo = self.get_ciclo()
            self.mes = self.get_mes()
            self.ano = self.get_ano()
        super(Lote, self).save()

    def delete(self, *args, **kwargs):
        pks = self.paquetes()
        super(Lote, self).delete()
        for p in pks:
            p.lotificado = False
            p.save()

    def __unicode__(self):
        return 'Lote ' + str(self.numero)


class control_entregas(base):
    pendientes = models.PositiveIntegerField(null=True)
    asignados = models.PositiveIntegerField(null=True)
    entregados = models.PositiveIntegerField(null=True)

    def paquetes(self):
        return Paquete.objects.filter(lotificado=True, cerrado=False)

    def entregas(self):
        return self.paquetes().filter(entrega=True, cerrado=False)

    def get_asignados(self):
        model = self.__class__
        if self.paquetes():
            if model.__name__ == 'Departamento':
                return self.paquetes().filter(iddepartemento=self.id).count()
            if model.__name__ == 'Municipio':
                return self.paquetes().filter(idmunicipio=self.id).count()
            if model.__name__ == 'Colector':
                return self.paquetes().filter(colector_id=self.id).count()

    def get_entregados(self):
        model = self.__class__
        if self.entregas():
            if model.__name__ == 'Departamento':
                return self.entregas().filter(iddepartemento=self.id).count()
            if model.__name__ == 'Municipio':
                return self.entregas().filter(idmunicipio=self.id).count()
            if model.__name__ == 'Colector':
                return self.entregas().filter(colector_id=self.id).count()
        else:
            return 0

    def actualizar_estadisticas_entrega(self):
        self.pendientes = self.get_asignados() - self.get_entregados()
        self.asignados = self.get_asignados()
        self.entregados = self.get_entregados()

    def save(self, *args, **kwargs):
        #self.actualizar_estadisticas_entrega()
        super(control_entregas, self).save()

    class Meta:
        abstract = True


class Colector(Entidad, control_entregas):
    foto = models.FileField(upload_to=get_media_url, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'colectores'


class Departamento(Entidad, control_entregas):
    codigo_telefonico = models.CharField(max_length=5, null=True, blank=True)


class Municipio(Entidad, control_entregas):
    departamento = models.ForeignKey(Departamento, null=True, blank=True)


class Barrio(Entidad):
    departamento = models.ForeignKey(Departamento, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, null=True, blank=True)


class Cliente(Entidad):
    departamento = models.ForeignKey(Departamento, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, null=True, blank=True)
    barrio = models.ForeignKey(Barrio, null=True, blank=True)
    contrato = models.PositiveIntegerField(null=True, blank=True)
    direccion = models.TextField(max_length=250, null=True, blank=True)
    distribuidor = models.CharField(max_length=150, null=True, blank=True)
    segmento = models.CharField(max_length=50, null=True, blank=True)
    tarifa = models.CharField(max_length=70, null=True, blank=True)
    servicio = models.CharField(max_length=70, null=True, blank=True)
    telefono_contacto = models.CharField(max_length=70, null=True, blank=True)
    valor_pagar = models.FloatField(null=True, blank=True)


def lotificar(paquetes):
    paquetes = paquetes.order_by('departamento', 'municipio', 'barrio',
        'direccion')
    lote_anterior = None
    for p in paquetes:
        if not p.lote:
            lote, created = Lote.objects.get_or_create(
                departamento=Departamento.objects.get(id=p.iddepartemento),
                municipio=Municipio.objects.get(id=p.idmunicipio),
                barrio=Barrio.objects.get(id=p.idbarrio), cerrado=False)
            p.lote = lote
            p.entrega = False
            p.save()

            if not lote_anterior:
                lote_anterior = Lote.objects.get(id=lote.id)
            else:
                if not lote_anterior.id == lote.id:
                    lote_anterior.cerrado = True
                    lote_anterior.save()
                    lote_anterior.ordenar_por_direccion()
                    lote_anterior = Lote.objects.get(id=lote.id)
    if lote_anterior:
        lote_anterior.cerrado = True
        lote_anterior.save()
        lote_anterior.ordenar_por_direccion()


def actualizar_estadisticas_entrega(entidades):
    for e in entidades:
        e.actualizar_estadisticas_entrega()
        e.save()


def corregir_ubicacion(comprobantes):
    mr = settings.MEDIA_ROOT
    for c in comprobantes:
        if c.comprobante:
            o = c.comprobante.path
            n = generar_ruta_comprobante(c, c.comprobante.name)
            d = os.path.join(mr, get_ruta(c))
            if not os.path.exists(d):
                os.makedirs(d)
            try:
                os.rename(o, os.path.join(mr, n))
            except:
                pass
            c.comprobante.name = n
            c.pod = c.comprobante
            c.save()


class impresion(models.Model):
    user = models.ForeignKey(User)
    fecha_verificacion = models.DateTimeField(auto_now=True)
    paquete = models.ForeignKey(Paquete)
    consecutivo = models.PositiveIntegerField()

    def __unicode__(self):
        return str(self.paquete)

    def cliente(self):
        return self.paquete.cliente

    cliente.allow_tags = True

    def grupo(self):
        return impresion.objects.filter(user=self.user)

    def get_consecutivo(self):
        if self.grupo():
            return self.grupo().aggregate(
                Max('consecutivo'))['consecutivo__max'] + 1
        else:
            return 1

    def save(self, *args, **kwars):
        self.consecutivo = self.get_consecutivo()
        super(impresion, self).save()

    class Meta:
        verbose_name_plural = 'impresiones'
        ordering = ['consecutivo']