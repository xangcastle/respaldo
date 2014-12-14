from django.contrib import admin
from moneycash.models import Item, Marca, Categoria, Cliente, Factura,\
    factura_detalle, Periodo, Serie, Sucursal, Caja, Bodega, Pago, Banco, Moneda,\
    Recibo, detalle_pago, pago_efectivo, pago_cheque, pago_tarjeta, pago_credito,\
    pago_transferencia, abonos_factura

class entidad_admin(admin.ModelAdmin):
    list_display = ('code','name')
    actions = ['activar','inactivar']
    ordering = ('code',)
    
    def inactivar(self, request, queryset):
        queryset.update(activo=False)
    inactivar.short_description = "Deactivate selected objects"

    def activar(self, request, queryset):
        queryset.update(activo=True)
    activar.short_description = "Activate selected objects"
    
class documento_admin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
        
class detalle_factura_tabular(admin.TabularInline):
    model = factura_detalle
    extra = 1
    classes = ('grp-collapse grp-open',)
    fields = ('item','codigo','descripcion','cantidad','costo_unitario','precio_unitario','total','descuento_unitario','precio_descontado','precio_descontado_total')
    
class factura_admin(documento_admin):
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('serie','fecha', 'numero','user'),('exento_iva','exento_iva_monto'),'alcaldia','retencion_ir')
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
    
class efectivo_tabular(admin.TabularInline):
    model = pago_efectivo
    extra = 1
    classes = ('grp-collapse grp-open',)
    fields = ('monto','moneda')
    
class cheque_tabular(admin.TabularInline):
    model = pago_cheque
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco','numero_cheque')
    
class tarjeta_tabular(admin.TabularInline):
    model = pago_tarjeta
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco')
    
class credito_tabular(admin.TabularInline):
    model = pago_credito
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco','cuenta')
    
class transferencia_tabular(admin.TabularInline):
    model = pago_transferencia
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('monto','moneda','banco','numero_transferencia')
    
class abonos_factura(admin.TabularInline):
    model = abonos_factura
    extra = 1
    classes = ('grp-collapse grp-closed',)
    fields = ('factura','total','monto','saldo')
    
class recibo_admin(documento_admin):
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('fecha', 'numero'),('cliente','nombre'),'concepto','monto')
        }),
        
    )
    inlines = [efectivo_tabular,cheque_tabular,tarjeta_tabular,transferencia_tabular,abonos_factura]
    
admin.site.register(Item,entidad_admin)
admin.site.register(Marca,entidad_admin)
admin.site.register(Categoria,entidad_admin)
admin.site.register(Cliente,entidad_admin)
admin.site.register(Periodo)
admin.site.register(Serie,entidad_admin)
admin.site.register(Sucursal,entidad_admin)
admin.site.register(Caja,entidad_admin)
admin.site.register(Bodega,entidad_admin)
admin.site.register(Pago,entidad_admin)
admin.site.register(Banco,entidad_admin)
admin.site.register(Moneda,entidad_admin)




