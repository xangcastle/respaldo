from django.db import models
from django.contrib.auth.models import User

class entidad(models.Model):
    code = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
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
        
class documento(models.Model):
    fecha = models.DateField()
    numero = models.PositiveIntegerField(null=True,blank=True)
    periodo = models.ForeignKey('Periodo',null=True,blank=True,related_name="%(app_label)s_%(class)s_periodo")
    user = models.ForeignKey(User,null=True,blank=True,related_name="%(app_label)s_%(class)s_user")
    sucursal = models.ForeignKey('Sucursal',null=True,blank=True,related_name="%(app_label)s_%(class)s_sucursal")
    autorizado = models.BooleanField(default=False)
    impreso = models.BooleanField(default=False)
    contabilizado = models.BooleanField(default=False)
    entregado = models.BooleanField(default=False)
    class Meta:
        abstract = True
        
class documento_caja(documento):
    caja = models.ForeignKey('Caja',null=True,blank=True,related_name="%(app_label)s_%(class)s_caja")
    cierre_caja = models.ForeignKey('CierreCaja',null=True,blank=True,related_name="%(app_label)s_%(class)s_cierre_caja")
    class Meta:
        abstract = True
        
class transaccion_monetaria(documento_caja):
    moneda = models.ForeignKey('Moneda',default=1,related_name="%(app_label)s_%(class)s_caja")
    monto = models.FloatField()
    class Meta:
        abstract = True
        