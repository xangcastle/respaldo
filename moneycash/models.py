from moneycash.base import models, entidad, documento, documento_caja,\
transaccion_monetaria, datos_generales


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

    class Meta:
        verbose_name_plural = "provedores"


class TipoCosto(entidad):
    pass


class Compra(documento):
    provedor = models.ForeignKey(Provedor)
    moneda = models.ForeignKey(Moneda, default=1)
    iva = models.FloatField(default=0.0)
    ir = models.FloatField(default=0.0, verbose_name="retencion del ir")
    al = models.FloatField(default=0.0, verbose_name="retencion de la alcaldia")
    total = models.FloatField(default=0.0)

    def detalles(self):
        return DetalleCompra.objects.filter(compra=self)

    def subtotal(self):
        st = 0.0
        if self.detalles():
            for d in self.detalles():
                st += (d.cantidad * d.precio)
        return st

    def save(self):
        self.total = self.subtotal() + self.iva
        super(Compra, self).save()

    class Meta:
        unique_together = ("provedor", "numero")


class BaseDetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, null=True, blank=True)
    item = models.ForeignKey('Item')
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    costo = models.FloatField(default=0)
    existencias = models.FloatField(default=0)
    costo_promedio = models.FloatField(default=0)
    costo_importacion = models.FloatField(default=0)
    costo_internacion = models.FloatField(default=0)
    recibido = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True


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
    cerrado = models.BooleanField(default=True)

    def __unicode__(self):
        return self.fecha_inicial.strftime("%B %Y")


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

