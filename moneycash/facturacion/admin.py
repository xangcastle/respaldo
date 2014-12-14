from moneycash.admin import admin, documento_admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline
from moneycash.models import factura_detalle
from moneycash.facturacion.models import Factura,Proforma

class detalle_factura_tabular(admin.TabularInline):
    model = factura_detalle
    extra = 1
    classes = ('grp-collapse grp-open',)
    fields = ('item','descripcion','cantidad','costo_unitario','precio_unitario','total','descuento_unitario','precio_descontado','precio_descontado_total')


class factura_admin(AjaxSelectAdmin):
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('serie','fecha', 'numero','user'),('exento_iva','exento_iva_monto'),'alcaldia','retencion_ir')
        }),
                         
        ('Datos del Cliente', {
        'classes': ('grp-collapse grp-open',),
        'fields': ('cliente',)
        }),
        ("Detalle Inlines", {"classes": ("placeholder factura_detalle_set-group",), "fields" : ()}),      
        ('Datos calculados y Totales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('subtotal','descuento', 'iva','total'),('retencion','costos','utilidad'),)
        }),
    )
    list_display = ('numero','fecha','cliente','subtotal','descuento','total')
    inlines = [detalle_factura_tabular]
    form = make_ajax_form(Factura, {'cliente': 'cliente'})

admin.site.register(Factura, factura_admin)
admin.site.register(Proforma, factura_admin)


