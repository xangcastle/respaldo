from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

#############
###EQUIPOS###
#############


class UnidadMedida(models.Model):
    nombre      =   models.CharField(max_length=100)
    simbolo     =   models.CharField(max_length=5)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"
    
class Item(models.Model):
    no_parte    =   models.CharField(max_length=25, verbose_name="Numero de Parte")
    nombre      =   models.CharField(max_length=200, verbose_name="Consumible o Repuesto")
    duracion    =   models.IntegerField()
    costo       =   models.FloatField()
    uni_medida  =   models.ForeignKey(UnidadMedida)
    def __unicode__(self):
        return self.nombre

class Consumible(models.Model):
    equipo      =   models.ForeignKey('Equipo')
    item        =   models.ForeignKey(Item)
    cantidad    =   models.FloatField()

class Marca(models.Model):
    OPCIONES_TIPO = (
                     ('OR','FABRICANTE ORIGINAL'),
                     ('GE','REMPLAZO GENERICO'),
                     )
    nombre = models.CharField(max_length=50,verbose_name="Marca")
    tipo = models.CharField(max_length=2,choices=OPCIONES_TIPO)
    def __unicode__(self):
        return self.nombre

class Equipo(models.Model):
    ubicacion   =   models.ForeignKey('Ubicacion',verbose_name="Ubicacion del Equipo",null=True,blank=True)
    marca       =   models.ForeignKey(Marca)
    modelo      =   models.CharField(max_length=50)
    serie       =   models.CharField(max_length=50)
    contador    =   models.IntegerField(default=0)
    minimo      =   models.IntegerField(default=0)
    velocidad   =   models.IntegerField(verbose_name="Copias x Minuto")
    papel       =   models.BooleanField(verbose_name="Incluye Papel")
    operador    =   models.BooleanField(verbose_name="Incluye Operador")
    precio_copia =  models.FloatField(verbose_name="Precio x Copias")
    comentarios =   models.CharField(max_length=400,null=True,blank=True)
    activo      =   models.BooleanField(default=True)
    consumibles =   models.ManyToManyField(Item,null=True,blank=True,through=Consumible)
    def __unicode__(self):
        return self.modelo + ' ' + self.serie
    def nombre_completo(self):
        return str(self.modelo) + '  -  ' + str(self.ubicacion)
    def area(self):
        a = ''
        if Area.objects.filter(equipo=self):
            if Area.objects.filter(equipo=self).count()==1:
                a = Area.objects.filter(equipo=self)[0].nombre
            else:
                a = self.ubicacion
        else:
            a = self.ubicacion
        return a
    def recibe(self):
        a = ''
        if Area.objects.filter(equipo=self):
            if Area.objects.filter(equipo=self).count()==1:
                a = Area.objects.filter(equipo=self)[0].responsable
            else:
                a = self.ubicacion
        return a

class AsistenciaTecnica(models.Model):
    fecha       =   models.DateField(auto_now=True)
    numero      =   models.IntegerField(verbose_name="Numero de Orden")
    tecnico     =   models.ForeignKey(User)
    equipo      =   models.ForeignKey(Equipo)
    contador    =   models.IntegerField()
    comentarios =   models.TextField(blank=True)    
    def partes_usadas(self):
        return Reemplazo.objects.filter(asis_tec=self)    
    def costo_total(self):
        return Reemplazo.objects.aggregate(costo=Sum('costo_consumible'))['costo']    
    def __unicode__(self):
        return str(self.numero) + str(self.tecnico.name)

class Reemplazo(models.Model):
    asis_tec    =   models.ForeignKey(AsistenciaTecnica)
    equipo      =   models.ForeignKey(Equipo)
    tecnico     =   models.ForeignKey(User)
    consumible  =   models.ForeignKey(Consumible)
    costo_consumible = models.FloatField()
    def __unicode__(self):
        return str(self.fecha)
    class Meta:
        verbose_name = 'Reemplazo de partes o consumibles'
        verbose_name_plural = 'Reemplazo de partes o consumibles'


class Periodo(models.Model):
    fecha_inicial   =   models.DateField()
    fecha_final     =   models.DateField()
    cerrado         =   models.BooleanField()    
    def __unicode__(self):
        return 'Desde ' + str(self.fecha_inicial) + ' hasta ' + str(self.fecha_final)
    def recibos(self):
        return Recibo.objects.filter(periodo=self)
    def total_copias(self):
        total = 0
        if self.recibos():
            for r in self.recibos():
                total += r.total_copias()
        return total
    def total_dolares(self):
        total = 0.0
        if self.recibos():
            for r in self.recibos():
                total += r.total_copias() * r.precio_copia
        return round(total,2)
    def iva(self):
        return round((self.total_dolares() * 0.15),2)
    def total(self):
        return round((self.total_dolares() + self.iva()),2)
    
class Recibo(models.Model):
    periodo         =   models.ForeignKey(Periodo)
    equipo          =   models.ForeignKey(Equipo)
    contador_inicial =  models.IntegerField()
    contador_final =    models.IntegerField()
    precio_copia    =   models.FloatField()
    def __unicode__(self):
        return self.equipo.modelo + ' fecha : ' + str(self.periodo.fecha_final)
    def detalles(self):
        d = Detalle.objects.filter(recibo=self)
        return d
    def copia_detalles(self):
        total = 0
        if self.detalles():
            for d in self.detalles():
                total += d.cantidad
        return total
    def copia_contador(self):
        return self.contador_final - self.contador_inicial
    def total_copias(self):
        if self.detalles():
            return self.copia_detalles()
        else:
            return self.copia_contador()
    def total_dolares(self):
        return round((self.total_copias() * self.precio_copia),2)
    def serie(self):
        return self.equipo.serie
    def fecha_inicial(self):
        return self.periodo.fecha_inicial
    def fecha_final(self):
        return self.periodo.fecha_final
    def ubicacion(self):
        return self.equipo.ubicacion
    def area(self):
        return self.equipo.area()
            
class Ubicacion(models.Model):
    nombre      =   models.CharField(max_length=50)
    direccion   =   models.CharField(max_length=400)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Ubicaciones"
    
class Area(models.Model):
    ubicacion = models.ForeignKey(Ubicacion)
    nombre = models.CharField(max_length=50,verbose_name="Area")
    responsable = models.CharField(max_length=50,verbose_name="Responsable de Area")
    codigo = models.IntegerField(verbose_name='Unidad Ejecutora')
    equipo = models.ForeignKey(Equipo,verbose_name="Impresora por Defecto",null=True,blank=True)
    def __unicode__(self):
        return self.nombre
    def get_direccion(self):
        u = self.ubicacion.direccion
        return u
    direccion = property(get_direccion)
    
class Detalle(models.Model):
    recibo = models.ForeignKey(Recibo)
    area = models.ForeignKey(Area)
    cantidad =  models.IntegerField()
    
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Detalles por Area"

    
    

    

        

