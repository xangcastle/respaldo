# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from datetime import timedelta
from django.db import models
from django.db.models import Sum, Manager
from .middlewares import get_current_user


# ESTADOS DE DOCUMENTOS
class documento_autorizado(Manager):
    def get_queryset(self):
        return super(documento_autorizado, self).get_queryset().filter(
            autorizado=True)


class documento_no_autorizado(Manager):
    def get_queryset(self):
        return super(documento_no_autorizado, self).get_queryset().filter(
            autorizado=False)


class documento_impreso(documento_autorizado):
    def get_queryset(self):
        return super(documento_impreso, self).get_queryset().filter(
            impreso=True)


class documento_no_impreso(documento_autorizado):
    def get_queryset(self):
        return super(documento_no_impreso, self).get_queryset().filter(
            impreso=False)


class documento_entregado(documento_impreso):
    def get_queryset(self):
        return super(documento_entregado, self).get_queryset().filter(
            entregado=True)


class documento_no_entregado(documento_impreso):
    def get_queryset(self):
        return super(documento_no_entregado, self).get_queryset().filter(
            entregado=False)


class documento_contabilizado(documento_impreso):
    def get_queryset(self):
        return super(documento_contabilizado, self).get_queryset().filter(
            contabilizado=True)


class documento_no_contabilizado(documento_impreso):
    def get_queryset(self):
        return super(documento_no_contabilizado, self).get_queryset().filter(
            contabilizado=False)


class user_manager(Manager):
    def get_queryset(self):
        if str(get_current_user()) == 'AnonymousUser':
            return super(user_manager, self).get_queryset()
        else:
            return super(user_manager, self).get_queryset(
                ).filter(user=get_current_user())


class empresa_manager(Manager):
    def get_queryset(self):
        if str(get_current_user()) == 'AnonymousUser':
            return super(empresa_manager, self).get_queryset()
        else:
            if not get_current_user().empresa:
                return super(empresa_manager, self).get_queryset()
            else:
                return super(empresa_manager, self).get_queryset(
                    ).filter(empresa=get_current_user().empresa)


class datos_generales(models.Model):
    identificacion = models.CharField(max_length=25, null=True, blank=True,
        verbose_name="ruc/cedula")
    telefono = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class entidad(models.Model):
    code = models.CharField(max_length=25, null=True, blank=True,
        verbose_name="codigo")
    name = models.CharField(max_length=100, verbose_name="nombre")
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

    class Meta:
        abstract = True
        ordering = ['name']


class documento(models.Model):
    fecha = models.DateField()
    numero = models.PositiveIntegerField(null=True, blank=True)
    periodo = models.ForeignKey('Periodo', null=True, blank=True,
        related_name="%(app_label)s_%(class)s_periodo")
    user = models.ForeignKey(User, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_user")
    sucursal = models.ForeignKey('Sucursal', null=True, blank=True,
        related_name="%(app_label)s_%(class)s_sucursal")
    autorizado = models.BooleanField(default=False)
    impreso = models.BooleanField(default=False)
    contabilizado = models.BooleanField(default=False)
    entregado = models.BooleanField(default=False)

    def __unicode__(self):
        if self.numero:
            return type(self).__name__ + " " + str(self.numero)
        else:
            return type(self).__name__

    class Meta:
        abstract = True


class documento_caja(documento):
    caja = models.ForeignKey('Caja', null=True, blank=True,
        related_name="%(app_label)s_%(class)s_caja")
    cierre_caja = models.ForeignKey('CierreCaja', null=True, blank=True,
        related_name="%(app_label)s_%(class)s_cierre_caja")

    class Meta:
        abstract = True


class transaccion_monetaria(documento_caja):
    moneda = models.ForeignKey('Moneda', default=1,
        related_name="%(app_label)s_%(class)s_caja")
    monto = models.FloatField()

    class Meta:
        abstract = True


class base_empresa_model(models.Model):
    empresa = models.ForeignKey('Empresa',
        related_name="%(app_label)s_%(class)s_empresa", null=True)
    objects = Manager()
    objects = empresa_manager()

    class Meta:
        abstract = True


class EmpresaModel(entidad, base_empresa_model):
    class Meta:
        abstract = True


class Empresa(entidad, datos_generales):
    pass

User.add_to_class('empresa', models.ForeignKey(Empresa, null=True))


class Pago(entidad):
    capitalizable = models.BooleanField(default=True,
    help_text="indica si este tipo de pago aplica en el cierre de caja")


class Banco(entidad):
    pass


class Moneda(entidad):
    pass


class tipo_movimiento(entidad):
    pass


class Cuenta_Banco(entidad):
    banco = models.ForeignKey(Banco)
    moneda = models.ForeignKey(Moneda)
    balance_inicial = models.FloatField()
    balance_actual = models.FloatField()
    es_tarjeta = models.BooleanField(default=False)


class tasa_cambio(models.Model):
    fecha = models.DateField()
    tipo_cambio = models.FloatField()

    def __unicode__(self):
        return str(self.tipo_cambio)


#class detMovimientosBanco(
    #IdMovBancos = models.ForeignKey(tipo_movimiento)
    #cuenta = models.ForeignKey(Cuenta_Banco)
	#IdCuenta integer NULL,
	#IdDeposito character varying(10) NULL,
	#IdRazonMovBanco integer NULL,
	#Documento character varying(20) NULL,
	#Descripcion character varying(200) NULL,
	#Fecha date NULL,
	#TipoMovimiento integer NULL,
	#Debito double precision NULL,
	#Credito double precision NULL,
	#SaldoAnterior double precision NULL,
	#SaldoActual double precision NULL,
	#Estado boolean NULL


class Serie(entidad):
    numero_inicial = models.PositiveIntegerField()


class Item(EmpresaModel):
    marca = models.ForeignKey('Marca', null=True, blank=True)
    categoria = models.ForeignKey('Categoria', null=True, blank=True)
    existencias = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    costo = models.FloatField(default=0)


class Marca(EmpresaModel):
    pass


class Categoria(EmpresaModel):
    parent = models.ForeignKey('self', null=True, blank=True)


class Provedor(datos_generales, EmpresaModel):
    TIPO_OPTIONS = (
      ('LO', 'NACIONAL'),
      ('EX', 'EXTRAJERO'),
    )
    tipo = models.CharField(max_length=2, choices=TIPO_OPTIONS, default='LO')
    tiempo_entrega = models.PositiveIntegerField(
        help_text="tiempo de entrega en dias para la mercaderia",
        verbose_name="tiempo de entrega", default=0)
    limite_credito = models.FloatField(null=True, blank=True)
    saldo = models.FloatField(default=0, blank=True,
        verbose_name="saldo inicial")
    plazo = models.PositiveIntegerField(default=0,
        help_text="plazo de credito expresado en cantidad de dias")
    #objects = Manager()
    #objects = empresa_manager()

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
                Sum('saldo'))['saldo__sum'], 2)) + " Cordobas"
            saldo.append(cordobas)
        if self.compras_credito_dolares():
            dolares = str(round(self.compras_credito_dolares().aggregate(
                Sum('saldo'))['saldo__sum'], 2)) + " Dolares"
            saldo.append(dolares)
        if len(saldo) > 0:
            return " y ".join(saldo)
        else:
            return 0

    get_saldo.short_description = "saldo"

    get_saldo.allow_tags = True


class TipoCosto(entidad):
    pass


class Compra(documento, base_empresa_model):
    TIPO_COMPRA = (('CO', 'CONTADO'), ('CR', 'CREDITO'))
    fecha_vence = models.DateField(null=True, blank=True,
        verbose_name="fecha de vencimiento",
        help_text="si se deja en blanco se aplica el plazo del provedor")
    comentarios = models.TextField(max_length=400, null=True, blank=True)
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
    abonado = models.FloatField(default=0.0)
    saldo = models.FloatField(default=0.0)
    objects = Manager()
    #objects = empresa_manager()

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


class BaseDetalleCompra(base_empresa_model):
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
    objects = Manager()
    objects = empresa_manager()

    def __unicode__(self):
        return str(self.item)

    class Meta:
        abstract = True
        verbose_name = "producto"


class DetalleCompra(BaseDetalleCompra):
    pass


class Poliza(documento, base_empresa_model):
    pass


#class poliza_producto(BaseDetalleCompra):
    #poliza = models.ForeignKey(Poliza)

    #class Meta:
        #managed = False


class DetallePoliza(base_empresa_model):
    poliza = models.ForeignKey(Poliza)
    factura = models.ForeignKey(Compra)
    tipo_costo = models.ForeignKey(TipoCosto)


class Sucursal(entidad, base_empresa_model):
    class Meta:
        verbose_name_plural = "sucursales"


class Caja(entidad, base_empresa_model):
    sucursal = models.ForeignKey(Sucursal)
    series = models.ManyToManyField(Serie)


class CierreCaja(documento, base_empresa_model):
    caja = models.ForeignKey(Caja)
    apertura = models.DateTimeField(null=True, blank=True)
    saldo_inicial = models.FloatField(default=0)
    cierre = models.DateTimeField(null=True, blank=True)
    saldo_final = models.FloatField(default=0)
    cerrado = models.BooleanField(default=False)


class Bodega(entidad, base_empresa_model):
    sucursal = models.ForeignKey(Sucursal)


class Cliente(entidad, base_empresa_model, datos_generales):
    bodegas = models.ManyToManyField(Bodega, null=True, blank=True)


class Contacto(entidad, base_empresa_model):
    cliente = models.ForeignKey(Cliente)
    cargo = models.CharField(max_length=100, null=True, blank=True,
         verbose_name="cargo que ocupa")
    telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


class Cuenta(entidad, base_empresa_model):
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


class Factura(documento_caja, base_empresa_model):
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


class Recibo(documento_caja, base_empresa_model):
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


class factura_detalle(base_empresa_model):
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


class detalle_pago(base_empresa_model):
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

