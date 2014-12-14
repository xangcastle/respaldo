from django.contrib import admin
from moneycash.models import Item, Marca, Categoria, Cliente, Factura,\
    factura_detalle, Periodo, Serie, Sucursal, Caja, Bodega, Pago, Banco, Moneda,\
    Recibo, detalle_pago

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
    fields = ('item','codigo','descripcion','cantidad','costo_unitario','precio_unitario','total','descuento_unitario','precio_descontado','precio_descontado_total')
    
class factura_admin(admin.ModelAdmin):
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('serie','fecha', 'numero','vendedor'),('exento_iva','exento_iva_monto'),'alcaldia','retencion_ir')
        }),
                         
        ('Datos del Cliente', {
        'classes': ('grp-collapse grp-open',),
        'fields': ('cliente',('nombre', 'telefono'),'direccion','comentarios')
        }),
        ("Detalle Inlines", {"classes": ("placeholder factura_detalle_set-group",), "fields" : ()}),      
        ('Datos calculados y Totales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('subtotal','descuento', 'iva','total'),('retencion','costos','utilidad'),)
        }),
    )
    
    inlines = [detalle_factura_tabular]
    
class detalle_pago_tabular(admin.TabularInline):
    model = detalle_pago
    extra = 1
    classes = ('grp-collapse grp-open',)
    
class recibo_admin(admin.ModelAdmin):
    inlines = [detalle_pago_tabular]


admin.site.register(Item,base_admin)
admin.site.register(Marca,base_admin)
admin.site.register(Categoria,base_admin)
admin.site.register(Cliente,base_admin)
admin.site.register(Factura)
admin.site.register(Periodo)
admin.site.register(Serie,base_admin)
admin.site.register(Sucursal,base_admin)
admin.site.register(Caja,base_admin)
admin.site.register(Bodega,base_admin)
admin.site.register(Pago,base_admin)
admin.site.register(Banco,base_admin)
admin.site.register(Moneda,base_admin)
admin.site.register(Recibo,recibo_admin)




