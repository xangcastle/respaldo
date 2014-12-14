from django.db import models
from django.contrib.auth.models import User


class entidad(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        if self.name:
            return self.name
        elif self.code:
            return str(self.code)
        elif self.code and self.name:
            return str(self.code) + ' ' + self.name
        else:
            return ''
    class Meta:
        abstract = True
        
class documento(models.Model):
    fecha = models.DateField()
    numero = models.PositiveIntegerField(null=True,blank=True)
    periodo = models.ForeignKey('Periodo',null=True,blank=True,related_name="%(app_label)s_%(class)s_periodo")
    user = models.ForeignKey(User,null=True,blank=True,related_name="%(app_label)s_%(class)s_user")
    sucursal = models.ForeignKey('Sucursal',null=True,blank=True,related_name="%(app_label)s_%(class)s_sucursal")
    class Meta:
        abstract = True
        
    def save(self):
        if not self.periodo:
            self.periodo = Periodo.objects.get(fecha_inicial__lte=self.fecha,fecha_final__gte=self.fecha)
        super(documento,self).save()
        
class documento_caja(documento):
    caja = models.ForeignKey('Caja',null=True,blank=True,related_name="%(app_label)s_%(class)s_caja")
    cierre_caja = models.ForeignKey('CierreCaja',null=True,blank=True,related_name="%(app_label)s_%(class)s_cierre_caja")
    class Meta:
        abstract = True
    
class Pago(entidad):
    capitalizable = models.BooleanField(default=True,help_text="indica si este tipo de pago aplica en el cierre de caja")

class Banco(entidad):
    pass

class Moneda(entidad):
    pass

class Serie(entidad):
    numero_inicial = models.PositiveIntegerField()
    
class Marca(entidad):
    pass

class Categoria(entidad):
    pass

class Item(entidad):
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
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
    apertura = models.DateTimeField(null=True,blank=True)
    saldo_inicial = models.FloatField(default=0)
    cierre = models.DateTimeField(null=True,blank=True)
    saldo_final = models.FloatField(default=0)
    cerrado = models.BooleanField(default=False)
    
class Bodega(entidad):
    sucursal = models.ForeignKey(Sucursal)
    
class Cliente(entidad):
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    bodegas = models.ManyToManyField(Bodega,null=True,blank=True)
    
class Cuenta(entidad):
    cliente = models.ForeignKey(Cliente)
    limite_credito = models.FloatField()
    plazo = models.PositiveIntegerField()
    saldo = models.FloatField(null=True,blank=True)
    
class Periodo(models.Model):
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cerrado = models.BooleanField(default=True)
    def __unicode__(self):
        return self.fecha_inicial.strftime("%B %Y")
    
class Factura(documento_caja):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    comentarios = models.CharField(max_length=200,null=True,blank=True)
    
    exento_iva = models.BooleanField(default=False)
    exento_iva_monto = models.FloatField(null=True,blank=True,verbose_name="porcentaje autorizado por la dgi")
    alcaldia = models.BooleanField(default=False)
    retencion_ir = models.BooleanField(default=False)
    
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)   
    iva = models.FloatField(default=0)
    total = models.FloatField(default=0)
    retencion = models.FloatField(default=0)
    costos = models.FloatField(default=0)
    utilidad = models.FloatField(default=0)
    
    impresa = models.BooleanField(default=False)
    contabilizada = models.BooleanField(default=False)
    autorizada = models.BooleanField(default=False)
    entregada = models.BooleanField(default=False)
    
    serie = models.ForeignKey(Serie,null=True,blank=True)
    cliente = models.ForeignKey(Cliente,null=True,blank=True)
    
    def __unicode__(self):
        if self.numero:
            return str(self.numero)
        elif self.nombre:
            return self.nombre
        else:
            return ''

class Recibo(documento_caja):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    concepto = models.CharField(max_length=200,null=True,blank=True)
    
    monto = models.FloatField(default=0)
    
    impreso = models.BooleanField(default=False)
    contabilizado = models.BooleanField(default=False)
    
    cliente = models.ForeignKey(Cliente,null=True,blank=True)
    
    def __unicode__(self):
        if self.numero:
            return str(self.numero)
        elif self.nombre:
            return self.nombre
        else:
            return ''
        
class Deposito(documento_caja):
    banco = models.ForeignKey(Banco)
    monto = models.FloatField()
        
class factura_detalle(models.Model):
    factura = models.ForeignKey(Factura)
    item = models.ForeignKey(Item,null=True,blank=True)
    marca = models.ForeignKey(Marca,null=True,blank=True)
    categoria = models.ForeignKey(Categoria,null=True,blank=True)
    
    codigo = models.CharField(max_length=25,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
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
    factura = models.ForeignKey(Factura,null=True,blank=True)
    recibo = models.ForeignKey(Recibo,null=True,blank=True)
    pago = models.ForeignKey(Pago) 
    monto = models.FloatField(default=0)
    total = models.FloatField(default=0)
    saldo = models.FloatField(default=0)
    moneda = models.ForeignKey(Moneda) 
    banco = models.ForeignKey(Banco,null=True,blank=True)
    numero_cheque = models.CharField(max_length=25,null=True,blank=True)
    numero_transferencia = models.CharField(max_length=25,null=True,blank=True)
    cuenta = models.ForeignKey(Cuenta,null=True,blank=True)
    def __unicode__(self):
        return ''
