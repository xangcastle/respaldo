from django.db.models import Sum, Min, Max
from moneycash.base import models, entidad, documento, documento_caja,\
transaccion_monetaria, datos_generales
from datetime import timedelta


class Pago(entidad):
    capitalizable = models.BooleanField(default=True,
    help_text="indica si este tipo de pago aplica en el cierre de caja")


class Banco(entidad):
    pass


class Moneda(entidad):
    pass


class Serie(entidad):
    numero_inicial = models.PositiveIntegerField()


class Marca(entidad):
    pass


class Categoria(entidad):
    parent = models.ForeignKey('self', null=True, blank=True)


class Provedor(entidad, datos_generales):
    TIPO_OPTIONS = (
      ('LO', 'NACIONAL'),
      ('EX', 'EXTRAJERO'),
    )
    tipo = models.CharField(max_length=2, choices=TIPO_OPTIONS, default='LO')
    tiempo_entrega = models.PositiveIntegerField(
        help_text="tiempo de entrega en dias para la mercaderia",
        verbose_name="tiempo de entrega", default=0)
    limite_credito = models.FloatField(null=True, blank=True)
    saldo = models.FloatField(null=True, blank=True)
    plazo = models.PositiveIntegerField(
        help_text="plazo de credito expresado en cantidad de dias")

    class Meta:
        verbose_name_plural = "provedores"

    def compras(self):
        return Compra.objects.filter(provedor=self)

    def compras_credito_cordobas(self):
        return self.compras().filter(tipo="CR", moneda=1)

    def compras_credito_dolares(self):
        return self.compras().filter(tipo="CR", moneda=2)

    def total_compras(self):
        if self.compras():
            return round(self.compras().aggregate(Sum('total'))['total__sum'],
                 2)
        else:
            return 0

    def get_saldo(self):
        saldo = []
        if self.compras_credito_cordobas():
            cordobas = str(round(self.compras_credito_cordobas().aggregate(
                Sum('total'))['total__sum'], 2)) + " Cordobas"
            saldo.append(cordobas)
        if self.compras_credito_dolares():
            dolares = str(round(self.compras_credito_dolares().aggregate(
                Sum('total'))['total__sum'], 2)) + " Dolares"
            saldo.append(dolares)
        if len(saldo) > 0:
            return " y ".join(saldo)
        else:
            return 0

    get_saldo.short_description = "saldo"

    get_saldo.allow_tags = True


class TipoCosto(entidad):
    pass


class Compra(documento):
    TIPO_COMPRA = (('CO', 'CONTADO'), ('CR', 'CREDITO'))
    fecha_vence = models.DateField(null=True, blank=True,
        verbose_name="fecha de vencimiento",
        help_text="si se deja en blanco se aplica el plazo del provedor")
    provedor = models.ForeignKey(Provedor)
    tipo = models.CharField(max_length=2, default="CR",
        verbose_name="tipo de pago de la compra", choices=TIPO_COMPRA)
    moneda = models.ForeignKey(Moneda, default=1)
    subtotal = models.FloatField(default=0.0)
    iva = models.FloatField(default=0.0)
    exento_iva = models.BooleanField(default=False)
    x_iva = models.FloatField(default=100, blank=True)
    ir = models.FloatField(default=0.0, verbose_name="retencion del ir")
    exento_ir = models.BooleanField(default=False)
    x_ir = models.FloatField(default=100, blank=True)
    al = models.FloatField(default=0.0, verbose_name="retencion de la alcaldia")
    exento_al = models.BooleanField(default=False,
        verbose_name="exento alcaldia")
    x_al = models.FloatField(default=100, blank=True)
    total = models.FloatField(default=0.0)

    def get_fecha_vence(self):
        if self.tipo == "CO":
            return None
        if self.tipo == "CR" and self.fecha_vence \
        and self.fecha_vence > self.fecha:
            return self.fecha_vence
        if self.tipo == "CR" and not self.fecha_vence:
            return self.fecha + timedelta(days=self.provedor.plazo)
        if self.fecha_vence and self.fecha > self.fecha_vence \
        and self.tipo == "CR":
            return self.fecha + timedelta(days=self.provedor.plazo)

    def save(self):
        self.fecha_vence = self.get_fecha_vence()
        super(Compra, self).save()

    class Meta:
        unique_together = ("provedor", "numero")
        #db_table = "moneycash_compras_compra"


class BaseDetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, null=True, blank=True)
    item = models.ForeignKey('Item')
    cantidad = models.FloatField(default=1)
    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    costo = models.FloatField(default=0)
    existencias = models.FloatField(default=0)
    costo_promedio = models.FloatField(default=0)
    costo_importacion = models.FloatField(default=0)
    costo_internacion = models.FloatField(default=0)
    recibido = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return str(self.item)

    class Meta:
        abstract = True
        verbose_name = "producto"


class DetalleCompra(BaseDetalleCompra):
    pass


class Poliza(documento):
    pass


#class poliza_producto(BaseDetalleCompra):
    #poliza = models.ForeignKey(Poliza)

    #class Meta:
        #managed = False


class DetallePoliza(models.Model):
    poliza = models.ForeignKey(Poliza)
    factura = models.ForeignKey(Compra)
    tipo_costo = models.ForeignKey(TipoCosto)


class Item(entidad):
    marca = models.ForeignKey(Marca, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    existencias = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    def compras(self):
        return DetalleCompra.objects.filter(item=self)

    def total_compras(self):
        if self.compras():
            return self.compras().aggregate(Sum('cantidad'))['cantidad__sum']
        else:
            return 0.0

    def precio_min(self):
        if self.compras():
            return self.compras().aggregate(Min('precio'))['precio__min']
        else:
            return 0.0

    def precio_max(self):
        if self.compras():
            return self.compras().aggregate(Max('precio'))['precio__max']
        else:
            return 0.0

class Sucursal(entidad):
    class Meta:
        verbose_name_plural = "sucursales"


class Caja(entidad):
    sucursal = models.ForeignKey(Sucursal)
    series = models.ManyToManyField(Serie)


class CierreCaja(documento):
    caja = models.ForeignKey(Caja)
    apertura = models.DateTimeField(null=True, blank=True)
    saldo_inicial = models.FloatField(default=0)
    cierre = models.DateTimeField(null=True, blank=True)
    saldo_final = models.FloatField(default=0)
    cerrado = models.BooleanField(default=False)


class Bodega(entidad):
    sucursal = models.ForeignKey(Sucursal)


class Cliente(entidad, datos_generales):
    bodegas = models.ManyToManyField(Bodega, null=True, blank=True)


class Contacto(entidad):
    cliente = models.ForeignKey(Cliente)
    cargo = models.CharField(max_length=100, null=True, blank=True,
         verbose_name="cargo que ocupa")
    telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


class Cuenta(entidad):
    numero_cuenta = models.CharField(max_length=25)
    cliente = models.ForeignKey(Cliente)
    limite_credito = models.FloatField()
    plazo = models.PositiveIntegerField()
    saldo = models.FloatField(null=True, blank=True)


class Periodo(models.Model):
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cerrado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.fecha_inicial.strftime("%B %Y")

    class Meta:
        ordering = ['-fecha_final']

    def compras(self):
        return Compra.objects.filter(periodo=self)

    def iva_pagado(self):
        if self.compras():
            return self.compras().aggregate(Sum('iva'))['iva__sum']
        else:
            return 0.0

    def ir_cobrado(self):
        if self.compras():
            return self.compras().aggregate(Sum('ir'))['ir__sum']
        else:
            return 0.0


class Factura(documento_caja):
    cliente = models.ForeignKey(Cliente, null=True, blank=True,
    help_text="BUSCAR CLIENTE")
    exento_iva = models.BooleanField(default=False)
    exento_iva_monto = models.FloatField(null=True, blank=True,
        verbose_name="porcentaje autorizado por la dgi")
    alcaldia = models.BooleanField(default=False)
    retencion_ir = models.BooleanField(default=False)
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    total = models.FloatField(default=0)
    retencion = models.FloatField(default=0)
    costos = models.FloatField(default=0)
    utilidad = models.FloatField(default=0)
    serie = models.ForeignKey(Serie, null=True, blank=True)

    def __unicode__(self):
        if self.numero:
            return str(self.numero)
        elif self.nombre:
            return self.nombre
        else:
            return ''


class Recibo(documento_caja):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    concepto = models.CharField(max_length=200, null=True, blank=True)
    monto = models.FloatField(default=0)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)

    def __unicode__(self):
        if self.numero:
            return str(self.numero)
        elif self.nombre:
            return self.nombre
        else:
            return ''


class Deposito(transaccion_monetaria):
    banco = models.ForeignKey(Banco)


class factura_detalle(models.Model):
    factura = models.ForeignKey(Factura)
    item = models.ForeignKey(Item, null=True, blank=True)
    marca = models.ForeignKey(Marca, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    codigo = models.CharField(max_length=25, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    cantidad = models.FloatField(default=0)
    descuento_unitario = models.FloatField(default=0)
    precio_unitario = models.FloatField(default=0)
    costo_unitario = models.FloatField(default=0)
    precio_descontado = models.FloatField(default=0)
    total = models.FloatField(default=0)
    descuento_total = models.FloatField(default=0)
    precio_descontado_total = models.FloatField(default=0)
    costo_total = models.FloatField(default=0)
    utilidad = models.FloatField(default=0)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = 'productos y/o servicios'

    def __unicode__(self):
        return ''


class detalle_pago(models.Model):
    factura = models.ForeignKey(Factura, null=True, blank=True)
    recibo = models.ForeignKey(Recibo, null=True, blank=True)
    pago = models.ForeignKey(Pago)
    monto = models.FloatField(default=0)
    total = models.FloatField(default=0)
    saldo = models.FloatField(default=0)
    moneda = models.ForeignKey(Moneda)
    banco = models.ForeignKey(Banco, null=True, blank=True)
    numero_cheque = models.CharField(max_length=25, null=True, blank=True)
    numero_transferencia = models.CharField(max_length=25, null=True,
        blank=True)
    cuenta = models.ForeignKey(Cuenta, null=True, blank=True)

    def __unicode__(self):
        return ''

