from django.contrib import admin
from moneycash.models import Item, Marca, Categoria, Cliente, Factura,\
    factura_detalle, Periodo, Serie, Sucursal, Caja, Bodega

class base_admin(admin.ModelAdmin):
    list_display = ('code','name')
    actions = ['activar','inactivar']
    ordering = ('code',)
    def inactivar(self, request, queryset):
        queryset.update(activo=False)
    inactivar.short_description = "Deactivate selected objects"

    def activar(self, request, queryset):
        queryset.update(activo=True)
    activar.short_description = "Activate selected objects"
class detalle_factura_tabular(admin.TabularInline):
    model = factura_detalle
    extra = 1
    classes = ('grp-collapse grp-open',)
    fields = ('item','cantidad','costo_unitario','precio_unitario','total','descuento_unitario','precio_descontado','precio_descontado_total')
    
class factura_admin(admin.ModelAdmin):
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('serie','fecha', 'numero','vendedor'),)
        }),
                         
        ('Datos del Cliente', {
        'classes': ('grp-collapse grp-open',),
        'fields': ('cliente',('nombre', 'telefono'),'direccion','comentarios')
        }),
    )
    
    inlines = [detalle_factura_tabular]

admin.site.register(Item,base_admin)
admin.site.register(Marca,base_admin)
admin.site.register(Categoria,base_admin)
admin.site.register(Cliente,base_admin)
admin.site.register(Factura,factura_admin)
admin.site.register(Periodo)
admin.site.register(Serie,base_admin)
admin.site.register(Sucursal,base_admin)
admin.site.register(Caja,base_admin)
admin.site.register(Bodega,base_admin)



