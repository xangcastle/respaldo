# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class BodegaKardex(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateTimeField()
    cantidad = models.FloatField()
    existencia = models.FloatField()
    saldo = models.FloatField()
    costo = models.FloatField()
    costo_promedio = models.FloatField()
    bodega = models.ForeignKey('MoneycashBodega')
    producto_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bodega_kardex'


class ComprasCategoria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_categoria'


class ComprasCompra(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    periodo = models.ForeignKey('MoneycashPeriodo', blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    sucursal = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    autorizado = models.BooleanField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    fecha_vence = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True)
    proveedor = models.ForeignKey('ComprasProveedor')
    tipo = models.CharField(max_length=2)
    moneda = models.ForeignKey('MoneycashMoneda')
    subtotal = models.FloatField()
    iva = models.FloatField()
    exento_iva = models.BooleanField()
    x_iva = models.FloatField()
    ir = models.FloatField()
    exento_ir = models.BooleanField()
    x_ir = models.FloatField()
    al = models.FloatField()
    exento_al = models.BooleanField()
    x_al = models.FloatField()
    total = models.FloatField()
    abonado = models.FloatField()
    saldo = models.FloatField()
    descuento = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_compra'


class ComprasCompraDetalle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    compra = models.ForeignKey(ComprasCompra, blank=True, null=True)
    producto = models.ForeignKey('ComprasProducto')
    cantidad = models.FloatField()
    existencias = models.FloatField()
    saldo = models.FloatField()
    precio = models.FloatField()
    descuento = models.FloatField()
    costo_entrada = models.FloatField()
    costo_promedio = models.FloatField()
    costo_importacion = models.FloatField()
    costo_internacion = models.FloatField()
    recibido = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_compra_detalle'


class ComprasMarca(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'compras_marca'


class ComprasProducto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    marca = models.ForeignKey(ComprasMarca, blank=True, null=True)
    categoria = models.ForeignKey(ComprasCategoria, blank=True, null=True)
    existencias = models.FloatField()
    descuento = models.FloatField()
    precio = models.FloatField()
    costo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'compras_producto'


class ComprasProveedor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identificacion = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    tipo = models.CharField(max_length=2)
    tiempo_entrega = models.IntegerField(blank=True, null=True)
    limite_credito = models.FloatField(blank=True, null=True)
    saldo = models.FloatField()
    plazo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_proveedor'


class ContabilidadBalanza(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saldo_inicial = models.FloatField()
    saldo_final = models.FloatField()
    cuenta = models.ForeignKey('ContabilidadCuenta')
    periodo = models.ForeignKey('ContabilidadPeriodo')

    class Meta:
        managed = False
        db_table = 'contabilidad_balanza'


class ContabilidadComprobante(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    periodo_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    concepto = models.TextField()
    sumas_iguales = models.BooleanField()
    total_debe = models.FloatField()
    total_haber = models.FloatField()
    code = models.CharField(max_length=30, blank=True)
    sucursal = models.CharField(max_length=65, blank=True)
    diferencia = models.FloatField()

    class Meta:
        managed = False
        db_table = 'contabilidad_comprobante'


class ContabilidadComprobanteDetalle(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    comprobante_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=-1, blank=True)
    name = models.CharField(max_length=100, blank=True)
    parcial = models.FloatField(blank=True, null=True)
    debe = models.FloatField(blank=True, null=True)
    haber = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contabilidad_comprobante_detalle'


class ContabilidadCuenta(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.NullBooleanField()
    saldo = models.FloatField()
    cuenta = models.ForeignKey('self', blank=True, null=True)
    naturaleza = models.CharField(max_length=2)
    saldo_actual = models.FloatField()

    class Meta:
        managed = False
        db_table = 'contabilidad_cuenta'


class ContabilidadKardex(models.Model):
    fecha = models.DateField(blank=True, null=True)
    codigo = models.CharField(max_length=30, blank=True)
    concepto = models.TextField(blank=True)
    code = models.CharField(max_length=25, blank=True)
    mayor = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    debe = models.FloatField(blank=True, null=True)
    haber = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contabilidad_kardex'


class ContabilidadMigracion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    poliza = models.CharField(max_length=30, blank=True)
    concepto = models.TextField()
    sucursal = models.CharField(max_length=65, blank=True)
    numero_cuenta = models.CharField(max_length=30, blank=True)
    nombre_cuenta = models.CharField(max_length=65, blank=True)
    debe = models.FloatField()
    haber = models.FloatField()

    class Meta:
        managed = False
        db_table = 'contabilidad_migracion'


class ContabilidadMovimiento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    debe = models.FloatField()
    haber = models.FloatField()
    comprobante = models.ForeignKey(ContabilidadComprobante)
    cuenta = models.ForeignKey(ContabilidadCuenta)
    periodo = models.ForeignKey('ContabilidadPeriodo')

    class Meta:
        managed = False
        db_table = 'contabilidad_movimiento'


class ContabilidadPeriodo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cerrado = models.BooleanField()
    code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contabilidad_periodo'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class MetropolitanaBarrio(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    departamento = models.ForeignKey('MetropolitanaDepartamento', blank=True, null=True)
    municipio = models.ForeignKey('MetropolitanaMunicipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metropolitana_barrio'


class MetropolitanaCliente(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    contrato = models.IntegerField(blank=True, null=True)
    direccion = models.TextField(blank=True)
    distribuidor = models.CharField(max_length=150, blank=True)
    segmento = models.CharField(max_length=50, blank=True)
    tarifa = models.CharField(max_length=70, blank=True)
    telefono_contacto = models.CharField(max_length=70, blank=True)
    barrio = models.ForeignKey(MetropolitanaBarrio, blank=True, null=True)
    departamento = models.ForeignKey('MetropolitanaDepartamento', blank=True, null=True)
    municipio = models.ForeignKey('MetropolitanaMunicipio', blank=True, null=True)
    valor_pagar = models.FloatField(blank=True, null=True)
    servicio = models.CharField(max_length=70, blank=True)

    class Meta:
        managed = False
        db_table = 'metropolitana_cliente'


class MetropolitanaColector(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    asignados = models.IntegerField(blank=True, null=True)
    entregados = models.IntegerField(blank=True, null=True)
    pendientes = models.IntegerField(blank=True, null=True)
    foto = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'metropolitana_colector'


class MetropolitanaDepartamento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    asignados = models.IntegerField(blank=True, null=True)
    entregados = models.IntegerField(blank=True, null=True)
    pendientes = models.IntegerField(blank=True, null=True)
    codigo_telefonico = models.CharField(max_length=5, blank=True)

    class Meta:
        managed = False
        db_table = 'metropolitana_departamento'


class MetropolitanaLote(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    numero = models.IntegerField()
    departamento = models.ForeignKey(MetropolitanaDepartamento, blank=True, null=True)
    municipio = models.ForeignKey('MetropolitanaMunicipio', blank=True, null=True)
    colector = models.ForeignKey(MetropolitanaColector, blank=True, null=True)
    cerrado = models.BooleanField()
    barrio = models.ForeignKey(MetropolitanaBarrio, blank=True, null=True)
    avance = models.CharField(max_length=10, blank=True)
    cantidad_paquetes = models.IntegerField(blank=True, null=True)
    entregados = models.IntegerField(blank=True, null=True)
    asignado = models.BooleanField()
    fecha = models.DateTimeField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    ciclo = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metropolitana_lote'


class MetropolitanaMunicipio(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    departamento = models.ForeignKey(MetropolitanaDepartamento, blank=True, null=True)
    asignados = models.IntegerField(blank=True, null=True)
    entregados = models.IntegerField(blank=True, null=True)
    pendientes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metropolitana_municipio'


class MetropolitanaPaquete(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    archivo = models.CharField(max_length=100, blank=True)
    consecutivo = models.IntegerField(blank=True, null=True)
    contrato = models.IntegerField(blank=True, null=True)
    factura = models.CharField(max_length=70, blank=True)
    ciclo = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    ano = models.IntegerField(blank=True, null=True)
    cliente = models.CharField(max_length=150, blank=True)
    direccion = models.TextField(blank=True)
    barrio = models.CharField(max_length=150, blank=True)
    municipio = models.CharField(max_length=150, blank=True)
    departamento = models.CharField(max_length=150, blank=True)
    distribuidor = models.CharField(max_length=150, blank=True)
    ruta = models.CharField(max_length=25, blank=True)
    zona = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True)
    tarifa = models.CharField(max_length=70, blank=True)
    idbarrio = models.IntegerField(blank=True, null=True)
    iddepartemento = models.IntegerField(blank=True, null=True)
    idmunicipio = models.IntegerField(blank=True, null=True)
    servicio = models.CharField(max_length=70, blank=True)
    cupon = models.IntegerField(blank=True, null=True)
    total_mes_factura = models.FloatField(blank=True, null=True)
    valor_pagar = models.FloatField(blank=True, null=True)
    entrega = models.BooleanField()
    numero_fiscal = models.IntegerField(blank=True, null=True)
    factura_interna = models.IntegerField(blank=True, null=True)
    telefono_contacto = models.CharField(max_length=70, blank=True)
    segmento = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2)
    colector = models.ForeignKey(MetropolitanaColector, blank=True, null=True)
    lote = models.ForeignKey(MetropolitanaLote, blank=True, null=True)
    lotificado = models.BooleanField()
    cerrado = models.BooleanField()
    comprobante = models.CharField(max_length=100, blank=True)
    barra = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'metropolitana_paquete'


class MoneycashBodega(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    sucursal = models.ForeignKey('MoneycashSucursal')

    class Meta:
        managed = False
        db_table = 'moneycash_bodega'


class MoneycashCategoria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_categoria'


class MoneycashCuenta(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    saldo = models.FloatField()
    cuenta_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_cuenta'


class MoneycashCuentaPeriodo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    saldo_inicial = models.FloatField()
    saldo_final = models.FloatField()
    cuenta = models.ForeignKey(MoneycashCuenta)
    periodo = models.ForeignKey('MoneycashPeriodo')

    class Meta:
        managed = False
        db_table = 'moneycash_cuenta_periodo'


class MoneycashDocumento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identificacion = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    fecha = models.DateTimeField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    autorizado = models.BooleanField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    moneda = models.ForeignKey('MoneycashMoneda', blank=True, null=True)
    periodo = models.ForeignKey('MoneycashPeriodo', blank=True, null=True)
    sucursal = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    tipodoc = models.ForeignKey('MoneycashTipodoc', blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    abonado = models.FloatField()
    al = models.FloatField()
    descuento = models.FloatField()
    exento_al = models.BooleanField()
    exento_ir = models.BooleanField()
    exento_iva = models.BooleanField()
    ir = models.FloatField()
    iva = models.FloatField()
    saldo = models.FloatField()
    subtotal = models.FloatField()
    total = models.FloatField()
    x_al = models.FloatField()
    x_ir = models.FloatField()
    x_iva = models.FloatField()
    bodega = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    cliente = models.ForeignKey('MoneycashSociocomercial', blank=True, null=True)
    fecha_vence = models.DateField(blank=True, null=True)
    forma_pago = models.CharField(max_length=2)
    proveedor = models.ForeignKey('MoneycashSociocomercial', blank=True, null=True)
    tc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_documento'


class MoneycashItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    marca = models.ForeignKey('MoneycashMarca', blank=True, null=True)
    categoria = models.ForeignKey(MoneycashCategoria, blank=True, null=True)
    costo = models.FloatField()
    descuento = models.FloatField()
    existencias = models.FloatField()
    precio = models.FloatField()
    almacenar = models.BooleanField()
    comprar = models.BooleanField()
    vender = models.BooleanField()
    factor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'moneycash_item'


class MoneycashKardex(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cantidad = models.FloatField()
    existencias = models.FloatField()
    saldo = models.FloatField()
    precio = models.FloatField()
    descuento = models.FloatField()
    costo_entrada = models.FloatField()
    costo_promedio = models.FloatField()
    costo_importacion = models.FloatField()
    costo_internacion = models.FloatField()
    recibido = models.FloatField(blank=True, null=True)
    documento = models.ForeignKey(MoneycashDocumento, blank=True, null=True)
    item = models.ForeignKey(MoneycashItem)
    bodega = models.ForeignKey(MoneycashBodega, blank=True, null=True)
    ubicacion = models.CharField(max_length=10, blank=True)
    costo_anterior = models.FloatField()

    class Meta:
        managed = False
        db_table = 'moneycash_kardex'


class MoneycashMarca(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_marca'


class MoneycashMoneda(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_moneda'


class MoneycashMovimiento(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    debe = models.FloatField()
    haber = models.FloatField()
    cuenta = models.ForeignKey(MoneycashCuenta)
    documento = models.ForeignKey(MoneycashDocumento)

    class Meta:
        managed = False
        db_table = 'moneycash_movimiento'


class MoneycashNumeracion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    numero_inicial = models.IntegerField()
    sucursal = models.ForeignKey('MoneycashSucursal')
    tipodoc = models.ForeignKey('MoneycashTipodoc')

    class Meta:
        managed = False
        db_table = 'moneycash_numeracion'


class MoneycashPeb(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    bodega_id = models.IntegerField(blank=True, null=True)
    existencias = models.FloatField(blank=True, null=True)
    ubicacion = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'moneycash_peb'


class MoneycashPeriodo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cerrado = models.BooleanField()
    fin_produccion = models.DateField(blank=True, null=True)
    inicio_produccion = models.DateField(blank=True, null=True)
    fin_ventas = models.DateField(blank=True, null=True)
    inicio_ventas = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_periodo'


class MoneycashRelacionComercial(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo_relacion = models.CharField(max_length=2)
    tiempo_entrega = models.IntegerField(blank=True, null=True)
    limite_credito = models.FloatField(blank=True, null=True)
    saldo = models.FloatField()
    plazo = models.IntegerField(blank=True, null=True)
    socio_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneycash_relacion_comercial'


class MoneycashSociocomercial(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identificacion = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_sociocomercial'


class MoneycashSucursal(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_sucursal'


class MoneycashTc(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    oficial = models.FloatField()
    moneda = models.ForeignKey(MoneycashMoneda)

    class Meta:
        managed = False
        db_table = 'moneycash_tc'


class MoneycashTipodoc(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    contabiliza = models.BooleanField()
    afectacion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneycash_tipodoc'


class MoneycashTotalPeriodo(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    periodo_id = models.IntegerField(blank=True, null=True)
    iva_pagado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ir_cobrado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    al_recaudado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    iva_contra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ir_pagado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    al_pagado = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_total_periodo'


class ProduccionArea(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    cliente = models.ForeignKey('ProduccionCliente')
    ubicacion = models.ForeignKey('ProduccionUbicacion')
    encargado = models.CharField(max_length=100)
    unidad_ejecutora = models.CharField(max_length=10)
    item = models.ForeignKey('ProduccionItem', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produccion_area'


class ProduccionAreaEquipos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    area = models.ForeignKey(ProduccionArea)
    equipo = models.ForeignKey('ProduccionEquipo')

    class Meta:
        managed = False
        db_table = 'produccion_area_equipos'


class ProduccionCategoria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'produccion_categoria'


class ProduccionCliente(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identificacion = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    limite_credito = models.FloatField(blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField()
    contacto = models.CharField(max_length=75, blank=True)
    nombre_area = models.CharField(max_length=75, blank=True)

    class Meta:
        managed = False
        db_table = 'produccion_cliente'


class ProduccionEquipo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    marca = models.ForeignKey('ProduccionMarca')
    modelo = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)
    velocidad = models.IntegerField()
    contador_inicial = models.IntegerField()
    contador_actual = models.IntegerField()
    vida_util = models.IntegerField()
    precio_copia = models.FloatField(blank=True, null=True)
    costo_compra = models.FloatField(blank=True, null=True)
    costo_copia = models.FloatField(blank=True, null=True)
    depreciacion_copia = models.FloatField(blank=True, null=True)
    precio_venta = models.FloatField(blank=True, null=True)
    valor_depreciado = models.FloatField(blank=True, null=True)
    ubicacion = models.ForeignKey('ProduccionUbicacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produccion_equipo'


class ProduccionEquipoPeriodo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    periodo = models.ForeignKey(MoneycashPeriodo)
    equipo = models.ForeignKey(ProduccionEquipo)
    contador_inicial = models.IntegerField()
    contador_final = models.IntegerField()
    copias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produccion_equipo_periodo'


class ProduccionFactura(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    autorizado = models.BooleanField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    exento_iva = models.BooleanField()
    exento_ir = models.BooleanField()
    subtotal = models.FloatField()
    descuento = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    ir = models.FloatField()
    al = models.FloatField()
    cliente_id = models.IntegerField()
    periodo = models.ForeignKey(ProduccionCliente, blank=True, null=True)
    sucursal = models.ForeignKey(MoneycashPeriodo, blank=True, null=True)
    user = models.ForeignKey(MoneycashSucursal, blank=True, null=True)
    fecha_vence = models.ForeignKey(AuthUser, db_column='fecha_vence', blank=True, null=True)
    saldo = models.FloatField()
    tipo = models.CharField(max_length=2)
    abonado = models.FloatField()
    comentarios = models.TextField(blank=True)
    exento_al = models.BooleanField()
    moneda_id = models.IntegerField()
    x_al = models.ForeignKey(MoneycashMoneda, db_column='x_al')
    x_ir = models.FloatField()
    x_iva = models.FloatField()
    tc = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produccion_factura'


class ProduccionFacturaDetalle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cantidad = models.FloatField()
    precio = models.FloatField()
    factura = models.ForeignKey(ProduccionFactura)
    item = models.ForeignKey('ProduccionItem')
    descuento = models.FloatField()
    total = models.FloatField()
    area = models.ForeignKey(ProduccionArea, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produccion_factura_detalle'


class ProduccionItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    precio = models.FloatField()
    categoria = models.ForeignKey(ProduccionCategoria)

    class Meta:
        managed = False
        db_table = 'produccion_item'


class ProduccionMarca(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'produccion_marca'


class ProduccionRecibo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    periodo = models.ForeignKey(MoneycashPeriodo, blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    sucursal = models.ForeignKey(MoneycashSucursal, blank=True, null=True)
    autorizado = models.BooleanField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    area = models.ForeignKey(ProduccionArea)
    copias = models.FloatField()
    importe = models.FloatField()
    tc = models.FloatField()

    class Meta:
        managed = False
        db_table = 'produccion_recibo'


class ProduccionReciboDetalle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    recibo = models.ForeignKey(ProduccionRecibo)
    equipo = models.ForeignKey(ProduccionEquipo)
    copias = models.FloatField()
    precio = models.FloatField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'produccion_recibo_detalle'


class ProduccionUbicacion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    user = models.ForeignKey(AuthUser)
    direccion = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'produccion_ubicacion'


class PruebaCliente(models.Model):
    id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100, blank=True)
    identificacion = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    tipo_relacion = models.CharField(max_length=2, blank=True)
    limite_credito = models.FloatField(blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)
    activo = models.NullBooleanField()
    socio_id = models.IntegerField(blank=True, null=True)
    tiempo_entrega = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prueba_cliente'


class RespaldoCuenta(models.Model):
    id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100, blank=True)
    activo = models.NullBooleanField()
    saldo = models.FloatField(blank=True, null=True)
    cuenta_id = models.IntegerField(blank=True, null=True)
    naturaleza = models.CharField(max_length=2, blank=True)
    saldo_actual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respaldo_cuenta'


class TarjetasAgencia(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tarjetas_agencia'


class TarjetasGrupo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tarjetas_grupo'


class TarjetasUsuario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    user = models.CharField(max_length=25)
    agencias = models.ForeignKey(TarjetasAgencia)
    grupo = models.ForeignKey(TarjetasGrupo)

    class Meta:
        managed = False
        db_table = 'tarjetas_usuario'
