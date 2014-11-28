from __future__ import unicode_literals

from django.db import models
from django.db.models import Sum
from datetime import timedelta
import time
from django.contrib.auth.models import User



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
    papel       =   models.BooleanField(default=False,verbose_name="Incluye Papel")
    operador    =   models.BooleanField(default=False,verbose_name="Incluye Operador")
    precio_copia =  models.FloatField(verbose_name="Precio x Copias")
    comentarios =   models.CharField(max_length=400,null=True,blank=True)
    activo      =   models.BooleanField(default=True)
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
            return round(self.costo / (self.vida_util),4)
    valor_de_depreciacion.allow_tags = True
    def valor_actual(self):
        if not self.costo or not self.vida_util:
            return 0
        else:
            return round((self.vida_util - self.contador) * self.valor_de_depreciacion(),4)

    valor_actual.allowtags = True

    class Meta:
        ordering = ('modelo',)

class Periodo(models.Model):

    def cuadro(self):
        return '<a href="/rentas/cuadro/%s">%s</a>' % (self.id,self.total())
    cuadro.allow_tags = True
    cuadro.short_description = "total a facturar"

    fecha_inicial   =   models.DateField()
    fecha_final     =   models.DateField()
    cerrado         =   models.BooleanField(default=False)

    class Meta:
        ordering = ('-fecha_inicial',)
    def __unicode__(self):
        return self.fecha_final.strftime("%B %Y")
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
    total_dolares.short_description = "producion bruta"
    def total_costos(self):
        total = 0.0
        if self.recibos():
            for r in self.recibos():
                total += r.total_costos()
        return round(total,2)
    def utilidad_total(self):
        return self.total_dolares() - self.total_costos()
    utilidad_total.short_description = "utilidad o perdida"
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

    periodo         =   models.ForeignKey(Periodo)
    equipo          =   models.ForeignKey(Equipo)
    contador_inicial=   models.IntegerField()
    contador_final  =   models.IntegerField(null=True)
    precio_copia    =   models.FloatField(verbose_name="precio por copia")
    meta            =   models.FloatField(null=True,blank=True,verbose_name="meta proyectada")
    costo_partes    =   models.FloatField(default=0.0,null=True,blank=True,verbose_name="costos de partes", help_text="suma de los costos de consumibles y partes usadas")
    costo_papel     =   models.FloatField(default=0.0,null=True,blank=True,verbose_name="costos de papel")
    costo_administrativo=   models.FloatField(default=0.0,null=True,blank=True,verbose_name="costos administrativos")
    depreciacion_activo =   models.FloatField(default=0.0,null=True,blank=True,verbose_name="costos de depreciasion de activos")
    tasa_cambio     =   models.FloatField(null=True,blank=True,verbose_name="tasa de cambio")
    
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
    def cumplimiento(self):
        if self.meta and self.meta > 0:
            return str(round((self.total_copias() * 100) / self.meta,2)) + '%'
        else:
            return '0%'

    def total_dolares(self):
        return round((self.total_copias() * self.precio_copia),2)
    def total_costos(self):
        return round(self.costo_papel + self.costo_partes + self.costo_administrativo + self.depreciacion_activo,2)
    def utilidad(self):
        return self.total_dolares() - self.total_costos()
    
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
    def fecha(self):
        return str(1000*time.mktime(self.periodo.fecha_final.timetuple()))
    
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
        
        
#### MODULO DE SITE
class Site(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True,verbose_name="nombre del site")
    encargado = models.ForeignKey(User,null=True,blank=True)
    ubicacion = models.ForeignKey(Ubicacion,null=True,blank=True)
    equipos = models.ManyToManyField(Equipo,null=True,blank=True)
    areas = models.ManyToManyField(Area,null=True,blank=True)
    
    def __unicode__(self):
        return self.name
## MODULO DE BODEGA

class Articulo(models.Model):
    codigo = models.CharField(max_length=30,null=True,blank=True)
    descripcion = models.CharField(max_length=300)
    marca = models.ForeignKey(Marca,null=True)
    costo = models.FloatField()
    caracteristicas = models.TextField(null=True,blank=True)
    
    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = "inventario"
       
    def __unicode__(self):
        return self.descripcion
    
    def entradas(self):
        return DetalleRequisa.entradas.filter(articulo=self)
    def total_entradas(self):
        if self.entradas():
            return self.entradas().aggregate(Sum('cantidad'))['cantidad__sum']
        else:
            return 0
    
    def salidas(self):
        return DetalleRequisa.salidas.filter(articulo=self)
    def total_salidas(self):
        if self.salidas():
            return self.salidas().aggregate(Sum('cantidad'))['cantidad__sum']
        else:
            return 0
    
    def existencias(self):
        return self.total_entradas() - self.total_salidas()
    existencias.allow_tags = True
    
    def inventario(self):
        return self.existencias() * self.costo
    inventario.allow_tags = True
    
class EntradaManager(models.Manager):
    def get_queryset(self):
        return super(EntradaManager,self).get_query_set().filter(tipo_requisa='EN')
class SalidaManager(models.Manager):
    def get_queryset(self):
        return super(SalidaManager,self).get_query_set().filter(tipo_requisa__in=('SA','CO'))
    
class Requisa(models.Model):
    TIPO_CHOICES = (
                    ('EN','REQUISA DE ENTRADA'),
                    ('SA','REQUISA DE SALIDA'),
                    ('CO','REQUISA DE CONSUMO'),
                    )
    
    tipo_requisa = models.CharField(max_length=2,choices=TIPO_CHOICES)
    fecha = models.DateField()
    periodo = models.ForeignKey(Periodo,null=True,blank=True)
    area = models.ForeignKey(Area,null=True,blank=True)
    recibido = models.CharField(max_length=300,null=True,blank=True)
    entregado = models.CharField(max_length=300,null=True,blank=True)
    site_origen = models.ForeignKey(Site,null=True,blank=True,related_name="requisa_site_origen")
    site_destino = models.ForeignKey(Site,null=True,blank=True,related_name="requisa_site_destino")
    objects = models.Manager()
    entradas = EntradaManager()
    salidas = SalidaManager()
    
    def __unicode__(self):
        return self.numero_requisa()
    
    def detalles(self):
        return DetalleRequisa.objects.filter(requisa=self)
    
    def str_detalle(self):
        texto = []
        if self.detalles():
            for d in self.detalles():
                item = str(d.cantidad) + ' ' + d.articulo.descripcion
                texto.append(item)
        return ', '.join(texto)
    str_detalle.short_description = "articulos"
    
    def costo_total(self):
        t = 0.0
        if self.detalles():
            for d in self.detalles():
                t += d.total()
        return t
    def print_tipo_requisa(self):
        if self.tipo_requisa == 'EN':
            return 'ENTRADA'
        else:
            return 'SALIDA'
    def numero_requisa(self):
        return 'requisa # ' +   str(self.id).zfill(6)
    def get_periodo(self):
        return Periodo.objects.get(fecha_inicial__lte=self.fecha, fecha_final__gte=self.fecha)
    
class EntradaArticuloManager(models.Manager):
    def get_queryset(self):
        return super(EntradaArticuloManager,self).get_query_set().filter(requisa__in=Requisa.entradas.all())
class SalidaArticuloManager(models.Manager):
    def get_queryset(self):
        return super(SalidaArticuloManager,self).get_query_set().filter(requisa__in=Requisa.salidas.all())    
class DetalleRequisa(models.Model):
    requisa = models.ForeignKey(Requisa)
    articulo =models.ForeignKey(Articulo)
    cantidad = models.FloatField()
    costo = models.FloatField()
    
    objects = models.Manager()
    entradas = EntradaArticuloManager()
    salidas = SalidaArticuloManager()
    
    def __unicode__(self):
        return ''
    def total(self):
        return self.cantidad * self.costo
    class Meta:
        verbose_name = 'articulo'