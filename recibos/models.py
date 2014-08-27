from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum,Max
from django.contrib.auth.models import User
from datetime import date, timedelta

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
        ordering = ('nombre',)
    
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

    def __unicode__(self):
        return self.item.nombre

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
    #datos del equipo
    ubicacion   =   models.ForeignKey('Ubicacion',verbose_name="Ubicacion del Equipo",null=True,blank=True)
    marca       =   models.ForeignKey(Marca)
    modelo      =   models.CharField(max_length=50)
    serie       =   models.CharField(max_length=50)
    contador    =   models.IntegerField(default=0)
    minimo      =   models.IntegerField(default=0)
    velocidad   =   models.IntegerField(verbose_name="Copias x Minuto")
    #datos de facturacion
    papel       =   models.BooleanField(verbose_name="Incluye Papel")
    operador    =   models.BooleanField(verbose_name="Incluye Operador")
    precio_copia =  models.FloatField(verbose_name="Precio x Copias")
    comentarios =   models.CharField(max_length=400,null=True,blank=True)
    activo      =   models.BooleanField(default=True)
    consumibles =   models.ManyToManyField(Item,null=True,blank=True,through=Consumible)
    #datos contables
    costo = models.FloatField(null=True,blank=True)
    vida_util = models.PositiveIntegerField(null=True,blank=True,help_text="vida util en cantidad de copias")
    
    def __unicode__(self):
        return self.modelo + ' - ' + self.serie
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
    def valor_de_depreciacion(self):
        if not self.costo or not self.vida_util:
            return 0
        else:
            return self.costo / (self.vida_util - self.contador)
    valor_de_depreciacion.allow_tags = True
    
    class Meta:
        ordering = ('modelo',)
    
class AsistenciaTecnica(models.Model):
    fecha       =   models.DateField(auto_now=True)
    numero      =   models.IntegerField(verbose_name="Numero de Orden")
    tecnico     =   models.ForeignKey(User)
    equipo      =   models.ForeignKey(Equipo)
    contador    =   models.IntegerField()
    comentarios =   models.TextField(blank=True)   
    
    def get_numero(self):
        if AsistenciaTecnica.objects.all().count() > 0:
            return AsistenciaTecnica.objects.all().aggregate(Max('numero'))['numero__max'] + 1
        else:
            return 1
    
    def save(self):
        self.numero = self.get_numero()
        super(AsistenciaTecnica,self).save()
    
    def partes_usadas(self):
        return Reemplazo.objects.filter(asis_tec=self)    
    def costo_total(self):
        return Reemplazo.objects.aggregate(costo=Sum('costo_consumible'))['costo']    
    def __unicode__(self):
        return str(self.numero) + str(self.tecnico.username)

class Reemplazo(models.Model):
    asis_tec    =   models.ForeignKey(AsistenciaTecnica)
    equipo      =   models.ForeignKey(Equipo)
    tecnico     =   models.ForeignKey(User)
    consumible  =   models.ForeignKey(Consumible)
    costo_consumible = models.FloatField()
    
    class Meta:
        verbose_name = 'Reemplazo de partes o consumibles'
        verbose_name_plural = 'Reemplazo de partes o consumibles'
        
    def save(self):
        self.equipo = self.asis_tec.equipo
        self.tecnico = self.asis_tec.tecnico
        super(Reemplazo,self).save()

class Periodo(models.Model):
    
    def cuadro(self):
        return '<a href="/rentas/cuadro/%s">Cuadro</a>' % (self.id)
    cuadro.allow_tags = True
    
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
    
    def equipos_activos(self):
        return Equipo.objects.filter(activo=True)
    
    def equipos_activos_sin_recibo(self):
        return self.equipos_activos().exclude(id__in=self.recibos().values_list('equipo',flat=True))
    
    def crear_recibo(self,equipo):
        if equipo:
            r = Recibo()
            r.periodo = self
            r.equipo = equipo
            r.contador_inicial = equipo.contador
            r.contador_final = equipo.contador
            r.precio_copia = equipo.precio_copia
            r.save()
    
    def generar_recibos(self):
        for e in self.equipos_activos_sin_recibo():
            self.crear_recibo(e)
            
    def abrir_periodo_siguiente(self):
        ps = Periodo()
        ps.fecha_inicial = self.fecha_final
        ps.fecha_final = self.fecha_final + timedelta(days=30)
        ps.cerrado = False
        ps.save()
        ps.generar_recibos()
        
    def cerrar(self):
        for r in self.recibos():
            e = r.equipo
            e.contador = r.contador_final
            e.save()
        self.abrir_periodo_siguiente()

class Recibo(models.Model):
    
    def imprimir(self):
        return '<a class="btn btn-mini btn-info" href="/rentas/recibo/%s/" align="center"><i class="icon-edit"></i>   Imprimir</a>' % (self.id)
    
    imprimir.allow_tags = True
    
    periodo         =   models.ForeignKey(Periodo)
    equipo          =   models.ForeignKey(Equipo)
    contador_inicial =  models.IntegerField()
    contador_final =    models.IntegerField(null=True)
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
    
    def copia_diferencia(self):
        if self.detalles():
            return self.copia_contador() - self.copia_detalles()
        else:
            return 0
    copia_diferencia.short_description = "Inconsitencias en el contador"
    
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
        return self.nombre + ' ' + self.responsable
    def get_direccion(self):
        u = self.ubicacion.direccion
        return u
    direccion = property(get_direccion)
    
    class Meta:
        ordering = ('nombre','responsable')
    
class Detalle(models.Model):
    recibo = models.ForeignKey(Recibo)
    area = models.ForeignKey(Area)
    cantidad =  models.IntegerField()
    
    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Detalles por Area"

    
    

    

        

