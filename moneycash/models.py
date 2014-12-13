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
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    bodegas = models.ManyToManyField(Bodega)
class Marca(base):
    pass
class Categoria(base):
    pass
class Item(base):
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
    existencias = models.FloatField()
    descuento = models.FloatField()
    precio = models.FloatField()
    costo = models.FloatField()


class Factura(models.Model):
    fecha = models.DateField()
    numero = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comentarios = models.CharField(max_length=200)
    
    exento_iva = models.BooleanField(default=True)
    exento_iva_monto = models.FloatField(null=True,blank=True)
    alcaldia = models.BooleanField(default=True)
    retencion_ir = models.BooleanField(default=True)
    
    subtotal = models.FloatField()
    descuento = models.FloatField()   
    iva = models.FloatField()
    total = models.FloatField()
    retencion = models.FloatField()
    costos = models.FloatField()
    utilidad = models.FloatField()
    
    impresa = models.BooleanField(default=True)
    contabilizada = models.BooleanField(default=True)
    autorizada = models.BooleanField(default=True)
    
    vendedor = models.FloatField(User)
    periodo = models.ForeignKey(Periodo)
    serie = models.ForeignKey(Serie)
    cliente = models.ForeignKey(Cliente)
    sucursal = models.FloatField(Sucursal)
    
    
    
class factura_detalle(models.Model):
    factura = models.ForeignKey(Factura)
    item = models.ForeignKey(Item)
    marca = models.ForeignKey(Marca)
    categoria = models.ForeignKey(Categoria)
    
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
    
    
    
    
    
    
    
    
    
