# -*- coding: latin-1 -*-
from django.db import models
from django.db.models import Max


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
    barra = models.CharField(max_length=30, null=True, blank=True)

    def link_comprobante(self):
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
        d, created = Departamento.objects.get_or_create(id=self.iddepartemento,
            name=self.departamento)
        #d.save()

        m, created = Municipio.objects.get_or_create(id=self.idmunicipio,
            name=self.municipio, departamento=d)
        #m.save()

        b, created = Barrio.objects.get_or_create(id=self.idbarrio,
        name=self.barrio, municipio=m, departamento=d)
        #b.save()

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

    def get_lotificado(self):
        if self.lote:
            return True
        else:
            return False

    def get_entregado(self):
        if self.comprobante:
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
        if self.lote \
        and self.entrega \
        and self.comprobante \
        and self.lote.asignado:
            return Colector.objects.get(id=self.lote.colector.id)
        else:
            return None

    def save(self, *args, **kwargs):
        self.lotificado = self.get_lotificado()
        self.entrega = self.get_entregado()
        self.cerrado = False
        self.barra = self.get_barra()
        self.colector = self.get_colector()
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

    def ordenar_paquetes(self):
        ps = self.paquetes().order_by('direccion')
        position = 0
        for p in ps:
            p.consecutivo = position
            p.save()
            position += 1

    def save(self, *args, **kwargs):
        if not self.numero:
            self.numero = self.get_numero()
        self.asignado = self.get_asignado()
        self.calcular()
        if self.cerrado:
            self.ciclo = self.get_ciclo()
            self.mes = self.get_mes()
            self.ano = self.get_ano()
        super(Lote, self).save()

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
                    lote_anterior.ordenar_paquetes()
                    lote_anterior = Lote.objects.get(id=lote.id)
    if lote_anterior:
        lote_anterior.cerrado = True
        lote_anterior.save()
        lote_anterior.ordenar_paquetes()


def actualizar_estadisticas_entrega(entidades):
    for e in entidades:
        e.actualizar_estadisticas_entrega()
        e.save()

# pid en el servidor = 12588