from django.contrib import admin
from recibos.models import Area,Equipo,Periodo,Recibo,Detalle,Ubicacion,Marca,Consumible,Item,UnidadMedida,AsistenciaTecnica,Reemplazo
from import_export.admin import ImportExportModelAdmin
from resources import Item_resouce

class DetalleInline(admin.TabularInline):
    model = Detalle
    extra = 0
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
    list_display = ('area','equipo','contador_inicial','contador_final','total_copias','copia_diferencia','imprimir')
    list_filter = ('periodo',)
    ordering = ('equipo',)
    inlines = [DetalleInline]
    list_editable = ('contador_inicial','contador_final',)
    
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha','equipo','tecnico','contador')
    
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo')
    inlines = [Equipoinline]
    
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicial','fecha_final','total_copias','total_dolares','cerrado','cuadro')
    list_filter = ('fecha_final','cerrado')
    inlines = [Reciboinline]
    
    def save_model(self, request, obj, form, change):
        obj.save()
        obj.generar_recibos()
        if obj.cerrado:
            obj.cerrar()
    
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
    
class Item_admin(ImportExportModelAdmin,admin.ModelAdmin):
    # resouce_class = Item_resouce
    list_display = ('no_parte','nombre','duracion','costo')
    search_fields = ('no_parte','nombre')

admin.site.register(Area,AreaAdmin)
admin.site.register(Equipo,EquipoAdmin)
admin.site.register(Periodo,PeriodoAdmin)
admin.site.register(Recibo,ReciboAdmin)
admin.site.register(Ubicacion,UbicacionAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Item,Item_admin)
admin.site.register(UnidadMedida)
admin.site.register(AsistenciaTecnica,asistencia_tecnica_admin)