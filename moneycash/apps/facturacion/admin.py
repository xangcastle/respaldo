from moneycash.admin import admin, documento_admin
from moneycash.models import factura_detalle
from moneycash.apps.facturacion.models import Factura,Proforma

class detalle_factura_tabular(admin.TabularInline):
    model = factura_detalle
    extra = 1
    classes = ('grp-collapse grp-open',)
    fields = ('item','descripcion','cantidad','costo_unitario','precio_unitario','total','descuento_unitario','precio_descontado','precio_descontado_total')


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
    list_display = ('numero','fecha','nombre','subtotal','descuento','total')
    inlines = [detalle_factura_tabular]

admin.site.register(Factura, factura_admin)
admin.site.register(Proforma, factura_admin)


