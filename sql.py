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
    permission_id = models.IntegerField()

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
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class ComprasCategoria(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    provedor_id = models.IntegerField(blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_categoria'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

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


class EstadisticasEquipo(models.Model):
    mes = models.TextField(blank=True)
    periodo = models.TextField(blank=True)
    modelo = models.CharField(max_length=50, blank=True)
    serie = models.CharField(max_length=50, blank=True)
    costo_activo = models.FloatField(blank=True, null=True)
    total_copias = models.IntegerField(blank=True, null=True)
    precio_copia = models.FloatField(blank=True, null=True)
    facturado = models.FloatField(blank=True, null=True)
    costo_partes = models.FloatField(blank=True, null=True)
    costo_papel = models.FloatField(blank=True, null=True)
    depreciacion_activo = models.FloatField(blank=True, null=True)
    costo_administrativo = models.FloatField(blank=True, null=True)
    total_costos = models.FloatField(blank=True, null=True)
    utilidad = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estadisticas_equipo'


class ModuleActivoFijo(models.Model):
    modelo = models.CharField(max_length=50, blank=True)
    serie = models.CharField(max_length=50, blank=True)
    costo_activo = models.FloatField(blank=True, null=True)
    valor_depreciado = models.FloatField(blank=True, null=True)
    valor_actual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_activo_fijo'


class MoneycashBanco(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_banco'


class MoneycashBodega(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    sucursal = models.ForeignKey('MoneycashSucursal')

    class Meta:
        managed = False
        db_table = 'moneycash_bodega'


class MoneycashCaja(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    sucursal = models.ForeignKey('MoneycashSucursal')

    class Meta:
        managed = False
        db_table = 'moneycash_caja'


class MoneycashCajaSeries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    caja = models.ForeignKey(MoneycashCaja)
    serie = models.ForeignKey('MoneycashSerie')

    class Meta:
        managed = False
        db_table = 'moneycash_caja_series'


class MoneycashCategoria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    parent = models.ForeignKey('self', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_categoria'


class MoneycashCierrecaja(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    apertura = models.DateTimeField(blank=True, null=True)
    cierre = models.DateTimeField(blank=True, null=True)
    cerrado = models.BooleanField()
    caja = models.ForeignKey(MoneycashCaja)
    periodo = models.ForeignKey('MoneycashPeriodo', blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    sucursal = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    saldo_final = models.FloatField()
    saldo_inicial = models.FloatField()
    autorizado = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    impreso = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_cierrecaja'


class MoneycashCliente(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    telefono = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    identificacion = models.CharField(max_length=25, blank=True)

    class Meta:
        managed = False
        db_table = 'moneycash_cliente'


class MoneycashClienteBodegas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cliente = models.ForeignKey(MoneycashCliente)
    bodega = models.ForeignKey(MoneycashBodega)

    class Meta:
        managed = False
        db_table = 'moneycash_cliente_bodegas'


class MoneycashCompra(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    autorizado = models.BooleanField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    periodo = models.ForeignKey('MoneycashPeriodo', blank=True, null=True)
    provedor = models.ForeignKey('MoneycashProvedor')
    sucursal = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    moneda = models.ForeignKey(AuthUser)
    al = models.ForeignKey('MoneycashMoneda', db_column='al')
    ir = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    exento_al = models.BooleanField()
    exento_ir = models.BooleanField()
    exento_iva = models.BooleanField()
    subtotal = models.FloatField()
    x_al = models.FloatField()
    x_ir = models.FloatField()
    x_iva = models.FloatField()

    class Meta:
        managed = False
        db_table = 'moneycash_compra'


class MoneycashContacto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    cargo = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=75, blank=True)
    cliente = models.ForeignKey(MoneycashCliente)

    class Meta:
        managed = False
        db_table = 'moneycash_contacto'


class MoneycashCuenta(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    limite_credito = models.FloatField()
    plazo = models.IntegerField()
    saldo = models.FloatField(blank=True, null=True)
    cliente = models.ForeignKey(MoneycashCliente)
    numero_cuenta = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'moneycash_cuenta'


class MoneycashDeposito(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    monto = models.FloatField()
    banco = models.ForeignKey(MoneycashBanco)
    caja = models.ForeignKey(MoneycashCaja, blank=True, null=True)
    cierre_caja = models.ForeignKey(MoneycashCierrecaja, blank=True, null=True)
    periodo = models.ForeignKey('MoneycashPeriodo', blank=True, null=True)
    sucursal = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)
    moneda = models.ForeignKey('MoneycashMoneda')
    autorizado = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    impreso = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_deposito'


class MoneycashDetallePago(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    monto = models.FloatField()
    numero_cheque = models.CharField(max_length=25, blank=True)
    numero_transferencia = models.CharField(max_length=25, blank=True)
    banco = models.ForeignKey(MoneycashBanco, blank=True, null=True)
    factura = models.ForeignKey('MoneycashFactura', blank=True, null=True)
    pago = models.ForeignKey('MoneycashPago')
    recibo = models.ForeignKey('MoneycashRecibo', blank=True, null=True)
    cuenta = models.ForeignKey(MoneycashCuenta, blank=True, null=True)
    moneda = models.ForeignKey('MoneycashMoneda')
    saldo = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'moneycash_detalle_pago'


class MoneycashDetallecompra(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cantidad = models.FloatField()
    precio = models.FloatField()
    descuento = models.FloatField()
    costo_promedio = models.FloatField()
    costo_importacion = models.FloatField()
    costo_internacion = models.FloatField()
    recibido = models.FloatField(blank=True, null=True)
    compra = models.ForeignKey(MoneycashCompra, blank=True, null=True)
    item = models.ForeignKey('MoneycashItem')
    costo = models.FloatField()
    existencias = models.FloatField()

    class Meta:
        managed = False
        db_table = 'moneycash_detallecompra'


class MoneycashDetallepoliza(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    factura = models.ForeignKey(MoneycashCompra)
    poliza = models.ForeignKey('MoneycashPoliza')
    tipo_costo = models.ForeignKey('MoneycashTipocosto')

    class Meta:
        managed = False
        db_table = 'moneycash_detallepoliza'


class MoneycashFactura(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    exento_iva = models.BooleanField()
    exento_iva_monto = models.FloatField(blank=True, null=True)
    alcaldia = models.BooleanField()
    retencion_ir = models.BooleanField()
    subtotal = models.FloatField()
    descuento = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    retencion = models.FloatField()
    costos = models.FloatField()
    utilidad = models.FloatField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    autorizado = models.BooleanField()
    cliente_id = models.IntegerField(blank=True, null=True)
    periodo_id = models.IntegerField(blank=True, null=True)
    serie_id = models.IntegerField(blank=True, null=True)
    sucursal_id = models.IntegerField(blank=True, null=True)
    entregado = models.BooleanField()
    cierre_caja_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(MoneycashCliente, blank=True, null=True)
    caja = models.ForeignKey('MoneycashPeriodo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_factura'


class MoneycashFacturaDetalle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cantidad = models.FloatField()
    descuento_unitario = models.FloatField()
    precio_unitario = models.FloatField()
    costo_unitario = models.FloatField()
    precio_descontado = models.FloatField()
    total = models.FloatField()
    descuento_total = models.FloatField()
    precio_descontado_total = models.FloatField()
    costo_total = models.FloatField()
    utilidad = models.FloatField()
    categoria = models.ForeignKey(MoneycashCategoria, blank=True, null=True)
    factura = models.ForeignKey(MoneycashFactura)
    item = models.ForeignKey('MoneycashItem', blank=True, null=True)
    marca = models.ForeignKey('MoneycashMarca', blank=True, null=True)
    codigo = models.CharField(max_length=25, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'moneycash_factura_detalle'


class MoneycashItem(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    existencias = models.FloatField()
    descuento = models.FloatField()
    precio = models.FloatField()
    costo = models.FloatField()
    categoria = models.ForeignKey(MoneycashCategoria, blank=True, null=True)
    marca = models.ForeignKey('MoneycashMarca', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_item'


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


class MoneycashPago(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    capitalizable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_pago'


class MoneycashPeriodo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cerrado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_periodo'


class MoneycashPoliza(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    autorizado = models.BooleanField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    entregado = models.BooleanField()
    periodo = models.ForeignKey(MoneycashPeriodo, blank=True, null=True)
    sucursal = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    user = models.ForeignKey(AuthUser, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_poliza'


class MoneycashProvedor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identificacion = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    tipo = models.CharField(max_length=2)
    tiempo_entrega = models.IntegerField()
    limite_credito = models.FloatField(blank=True, null=True)
    saldo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moneycash_provedor'


class MoneycashRecibo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True)
    concepto = models.CharField(max_length=200, blank=True)
    monto = models.FloatField()
    impreso = models.BooleanField()
    contabilizado = models.BooleanField()
    caja = models.ForeignKey(MoneycashCaja, blank=True, null=True)
    cliente_id = models.IntegerField(blank=True, null=True)
    periodo = models.ForeignKey(MoneycashCliente, blank=True, null=True)
    sucursal = models.ForeignKey(MoneycashPeriodo, blank=True, null=True)
    cierre_caja = models.ForeignKey('MoneycashSucursal', blank=True, null=True)
    user = models.ForeignKey(MoneycashCierrecaja, blank=True, null=True)
    autorizado = models.ForeignKey(AuthUser, db_column='autorizado')
    entregado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_recibo'


class MoneycashSerie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()
    numero_inicial = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneycash_serie'


class MoneycashSucursal(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_sucursal'


class MoneycashTipocosto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    code = models.CharField(max_length=25, blank=True)
    name = models.CharField(max_length=100)
    activo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'moneycash_tipocosto'


class MusicAuthor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'music_author'


class MusicBook(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    author = models.ForeignKey(MusicAuthor)
    title = models.CharField(max_length=100)
    about_group = models.ForeignKey('MusicGroup')

    class Meta:
        managed = False
        db_table = 'music_book'


class MusicBookMentionsPersons(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    book = models.ForeignKey(MusicBook)
    person = models.ForeignKey('MusicPerson')

    class Meta:
        managed = False
        db_table = 'music_book_mentions_persons'


class MusicGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=200)
    url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'music_group'


class MusicGroupMembers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(MusicGroup)
    person = models.ForeignKey('MusicPerson')

    class Meta:
        managed = False
        db_table = 'music_group_members'


class MusicLabel(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=200)
    owner = models.ForeignKey('MusicPerson', blank=True, null=True)
    url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'music_label'


class MusicPerson(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=75)

    class Meta:
        managed = False
        db_table = 'music_person'


class MusicRelease(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=100)
    catalog = models.CharField(max_length=100)
    group = models.ForeignKey(MusicGroup, blank=True, null=True)
    label = models.ForeignKey(MusicLabel)

    class Meta:
        managed = False
        db_table = 'music_release'


class MusicReleaseSongs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    release = models.ForeignKey(MusicRelease)
    song = models.ForeignKey('MusicSong')

    class Meta:
        managed = False
        db_table = 'music_release_songs'


class MusicSong(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=200)
    group = models.ForeignKey(MusicGroup)

    class Meta:
        managed = False
        db_table = 'music_song'


class RecibosArea(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ubicacion = models.ForeignKey('RecibosUbicacion')
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    codigo = models.IntegerField()
    equipo = models.ForeignKey('RecibosEquipo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_area'


class RecibosArticulo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(max_length=30, blank=True)
    descripcion = models.CharField(max_length=300)
    marca = models.ForeignKey('RecibosMarca', blank=True, null=True)
    costo = models.FloatField()
    caracteristicas = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'recibos_articulo'


class RecibosCambioPartes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cantidad = models.FloatField()
    costo = models.FloatField()
    refaccion = models.ForeignKey('RecibosRefaccion')
    servicio = models.ForeignKey('RecibosServicio')

    class Meta:
        managed = False
        db_table = 'recibos_cambio_partes'


class RecibosCategoria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100)
    comprar = models.BooleanField()
    vender = models.BooleanField()
    almacenar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'recibos_categoria'


class RecibosContacto(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=100, blank=True)
    cargo = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=75, blank=True)
    provedor = models.ForeignKey('RecibosProvedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_contacto'


class RecibosDetalle(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    recibo = models.ForeignKey('RecibosRecibo')
    area = models.ForeignKey(RecibosArea)
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recibos_detalle'


class RecibosDetallerequisa(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    requisa = models.ForeignKey('RecibosRequisa')
    articulo = models.ForeignKey(RecibosArticulo)
    cantidad = models.FloatField()
    costo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'recibos_detallerequisa'


class RecibosDtcompra(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cantidad = models.FloatField()
    precio = models.FloatField()
    factura = models.ForeignKey('RecibosFcompra')
    item = models.ForeignKey('RecibosRefaccion')

    class Meta:
        managed = False
        db_table = 'recibos_dtcompra'


class RecibosEquipo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ubicacion = models.ForeignKey('RecibosUbicacion', blank=True, null=True)
    marca = models.ForeignKey('RecibosMarca')
    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
    contador = models.IntegerField()
    minimo = models.IntegerField()
    velocidad = models.IntegerField()
    papel = models.BooleanField()
    operador = models.BooleanField()
    precio_copia = models.FloatField()
    comentarios = models.CharField(max_length=400, blank=True)
    activo = models.BooleanField()
    costo = models.FloatField(blank=True, null=True)
    vida_util = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_equipo'


class RecibosEquipoAreas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    equipo = models.ForeignKey(RecibosEquipo)
    area = models.ForeignKey(RecibosArea)

    class Meta:
        managed = False
        db_table = 'recibos_equipo_areas'


class RecibosFcompra(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField()
    provedor = models.ForeignKey('RecibosProvedor')
    moneda = models.ForeignKey('RecibosMoneda', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_fcompra'


class RecibosMarca(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'recibos_marca'


class RecibosMoneda(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    simbolo = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'recibos_moneda'


class RecibosPeriodo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cerrado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'recibos_periodo'


class RecibosProvedor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(max_length=20, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'recibos_provedor'


class RecibosRecibo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    periodo = models.ForeignKey(RecibosPeriodo)
    equipo = models.ForeignKey(RecibosEquipo)
    contador_inicial = models.IntegerField()
    contador_final = models.IntegerField()
    precio_copia = models.FloatField()
    meta = models.FloatField(blank=True, null=True)
    costo_partes = models.FloatField(blank=True, null=True)
    tasa_cambio = models.FloatField(blank=True, null=True)
    costo_administrativo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_recibo'


class RecibosReciboPapel(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    recibo_id = models.IntegerField(blank=True, null=True)
    articulo_id = models.IntegerField(blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    costo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_recibo_papel'


class RecibosRefaccion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(max_length=20, blank=True)
    descripcion = models.CharField(max_length=200, blank=True)
    costo = models.FloatField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    oem = models.CharField(max_length=20, blank=True)
    minimo = models.FloatField(blank=True, null=True)
    categoria = models.ForeignKey(RecibosCategoria, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_refaccion'


class RecibosRequisa(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo_requisa = models.CharField(max_length=2)
    fecha = models.DateField()
    area = models.ForeignKey(RecibosArea, blank=True, null=True)
    recibido = models.CharField(max_length=300, blank=True)
    entregado = models.CharField(max_length=300, blank=True)
    site_origen = models.ForeignKey('RecibosSite', blank=True, null=True)
    site_destino = models.ForeignKey('RecibosSite', blank=True, null=True)
    periodo = models.ForeignKey(RecibosPeriodo, blank=True, null=True)
    equipo = models.ForeignKey(RecibosEquipo, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_requisa'


class RecibosServicio(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    numero = models.IntegerField(blank=True, null=True)
    obserbaciones = models.TextField(blank=True)
    equipo = models.ForeignKey(RecibosEquipo, blank=True, null=True)
    periodo = models.ForeignKey(RecibosPeriodo, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_servicio'


class RecibosSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    encargado = models.ForeignKey(AuthUser, blank=True, null=True)
    ubicacion = models.ForeignKey('RecibosUbicacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibos_site'


class RecibosSiteAreas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    site = models.ForeignKey(RecibosSite)
    area = models.ForeignKey(RecibosArea)

    class Meta:
        managed = False
        db_table = 'recibos_site_areas'


class RecibosSiteEquipos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    site_id = models.IntegerField()
    equipo = models.ForeignKey(RecibosEquipo)

    class Meta:
        managed = False
        db_table = 'recibos_site_equipos'


class RecibosUbicacion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=400)

    class Meta:
        managed = False
        db_table = 'recibos_ubicacion'


class TotalActivoFijo(models.Model):
    costos_activos = models.FloatField(blank=True, null=True)
    monto_total_depreciado = models.FloatField(blank=True, null=True)
    valor_actual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'total_activo_fijo'


class ViewRecibosRecibo(models.Model):
    id = models.IntegerField(blank=True, null=True)
    periodo_id = models.IntegerField(blank=True, null=True)
    equipo_id = models.IntegerField(blank=True, null=True)
    contador_inicial = models.IntegerField(blank=True, null=True)
    contador_final = models.IntegerField(blank=True, null=True)
    precio_copia = models.FloatField(blank=True, null=True)
    meta = models.FloatField(blank=True, null=True)
    costo_partes = models.FloatField(blank=True, null=True)
    tasa_cambio = models.FloatField(blank=True, null=True)
    costo_administrativo = models.FloatField(blank=True, null=True)
    costo_papel = models.FloatField(blank=True, null=True)
    depreciacion_activo = models.FloatField(blank=True, null=True)
    total_copias = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'view_recibos_recibo'
