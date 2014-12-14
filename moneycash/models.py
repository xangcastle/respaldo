from django.db import models
from django.contrib.auth.models import User


class base(models.Model):
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
        
class Periodo(models.Model):
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    cerrado = models.BooleanField(default=True)
    def __unicode__(self):
        return self.fecha_inicial.strftime("%B %Y")
class Serie(base):
    numero_inicial = models.PositiveIntegerField()
class Sucursal(base):
    class Meta:
        verbose_name_plural = "sucursales"
class Caja(base):
    sucursal = models.ForeignKey(Sucursal)
    series = models.ManyToManyField(Serie)
class Bodega(base):
    sucursal = models.ForeignKey(Sucursal)
class Cliente(base):
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    bodegas = models.ManyToManyField(Bodega,null=True,blank=True)
class Marca(base):
    pass
class Categoria(base):
    pass
class Item(base):
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
    existencias = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    costo = models.FloatField(default=0)


class Factura(models.Model):
    fecha = models.DateField()
    numero = models.PositiveIntegerField(null=True,blank=True)
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
    
    vendedor = models.ForeignKey(User)
    periodo = models.ForeignKey(Periodo)
    serie = models.ForeignKey(Serie)
    cliente = models.ForeignKey(Cliente)
    sucursal = models.ForeignKey(Sucursal)
    
    def __unicode__(self):
        if self.numero:
            return str(self.numero)
        elif self.nombre:
            return self.nombre
        else:
            return ''
    
    
    
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
    
    
class Pago(base):
    pass

class Banco(base):
    pass

class Moneda(base):
    pass

class Recibo(models.Model):
    fecha = models.DateField()
    numero = models.PositiveIntegerField(null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
    concepto = models.CharField(max_length=200,null=True,blank=True)
    
    monto = models.FloatField(default=0)
    
    impreso = models.BooleanField(default=False)
    contabilizado = models.BooleanField(default=False)
    
    cajero = models.ForeignKey(User)
    periodo = models.ForeignKey(Periodo)
    cliente = models.ForeignKey(Cliente,null=True,blank=True)
    sucursal = models.ForeignKey(Sucursal)
    caja = models.ForeignKey(Caja)
    
    def __unicode__(self):
        if self.numero:
            return str(self.numero)
        elif self.nombre:
            return self.nombre
        else:
            return ''

class detalle_pago(models.Model):
    factura = models.ForeignKey(Factura,null=True,blank=True)
    recibo = models.ForeignKey(Recibo,null=True,blank=True)
    pago = models.ForeignKey(Pago) 
    monto = models.FloatField(default=0)
    banco = models.ForeignKey(Banco,null=True,blank=True)
    numero_cheque = models.CharField(max_length=25,null=True,blank=True)
    numero_transferencia = models.CharField(max_length=25,null=True,blank=True)
    def __unicode__(self):
        return ''
    
    
