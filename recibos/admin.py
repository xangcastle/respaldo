from django.contrib import admin
from recibos.models import Area,Equipo,Periodo,Recibo,Detalle,Ubicacion,Marca,Consumible,Item,UnidadMedida,AsistenciaTecnica,Reemplazo


class DetalleInline(admin.TabularInline):
    model = Detalle
class Equipoinline(admin.TabularInline):
    model = Equipo
class Areainline(admin.TabularInline):
    model = Area
class Reciboinline(admin.TabularInline):
    model = Recibo
class Consumibleinline(admin.TabularInline):
    model = Consumible
    
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre','responsable','codigo','equipo','direccion')
    list_filter = ('codigo','ubicacion')
    ordering = ('nombre','responsable','codigo')
    search_fields = ('nombre','responsable')

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('modelo','serie','contador','ubicacion','area','comentarios','activo')
    list_filter = ('ubicacion','activo')
    search_fields = ('modelo','serie')
    inlines = [Consumibleinline]
    
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion')
    ordering = ('nombre',)
    #inlines = [Areainline]
    
class ReciboAdmin(admin.ModelAdmin):
    list_display = ('area','ubicacion','equipo','contador_final','imprimir','precio_copia','total_dolares')
    list_filter = ('periodo',)
    ordering = ('equipo',)
    inlines = [DetalleInline]
    list_editable = ('contador_final',)
    
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha','equipo','tecnico','contador')
    
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo')
    inlines = [Equipoinline]
    
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicial','fecha_final','total_copias','total_dolares','cerrado','cuadro')
    list_filter = ('cerrado',)
    inlines = [Reciboinline]
    
    
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.save()
            equipos  = Equipo.objects.filter(activo=True)
            for e in equipos:
                r = Recibo()
                r.periodo = obj
                r.equipo = e
                r.precio_copia = e.precio_copia
                r.contador_inicial = e.contador
                r.contador_final = e.contador
                r.save()
            obj.save()
            
        if obj.cerrado == True:
            recibos = Recibo.objects.filter(periodo=obj)
            for r in recibos:
                e = r.equipo
                e.contador = r.contador_final
                e.save()
            obj.save()
    
class partes(admin.TabularInline):
    model = Reemplazo
    extra = 1
    exclude = ('equipo','tecnico')
    
class asistencia_tecnica_admin(admin.ModelAdmin):
    exclude = ('numero','tecnico')
    inlines = [partes]
    
    def save_model(self, request, obj, form, change):
        obj.tecnico = request.user
        obj.save()
        
        
admin.site.register(Area,AreaAdmin)
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(Recibo,ReciboAdmin)
admin.site.register(Ubicacion,UbicacionAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Item)
admin.site.register(UnidadMedida)
admin.site.register(AsistenciaTecnica,asistencia_tecnica_admin)