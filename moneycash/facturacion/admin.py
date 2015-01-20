from moneycash.admin import admin, documento_admin, entidad_admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline
from moneycash.models import factura_detalle
from moneycash.facturacion.models import Factura, Proforma, Cliente


class detalle_factura_tabular(AjaxSelectAdminTabularInline):
    model = factura_detalle
    extra = 1
    classes = ('grp-collapse grp-open',)
    fields = ('item', 'cantidad', 'precio_unitario', 'total',
        'descuento_unitario', 'precio_descontado', 'precio_descontado_total')
    readonly_fields = ('total', 'precio_descontado', 'precio_descontado_total')
    form = make_ajax_form(factura_detalle, {'item': 'item'})


class factura_admin(documento_admin, AjaxSelectAdmin):
    list_display = ('numero', 'fecha', 'provedor',
        'subtotal', 'iva', 'total', 'ir', 'al',)
    list_filter = ('periodo', 'cliente', 'tipo')
    fieldsets = (
        ('Datos de La compra', {'classes': ('grp-collapse grp-open',),
            'fields': (('numero', 'fecha', 'moneda'),
                ('tipo', 'fecha_vence'), 'comentarios', 'provedor',
                ('exento_iva', 'exento_ir', 'exento_al'))}),
        ("Detalle Inlines", {"classes":
            ("placeholder detalle_set-group",), "fields": ()}),
        ('Impuestos y totales', {'classes': ('grp-collapse grp-open',),
            'fields': (('iva', 'ir', 'al', 'total'),)}),
                )
    form = make_ajax_form(Factura, {'cliente': 'cliente'})
    readonly_fields = ('iva', 'ir', 'al', 'total')


class cliente_admin(entidad_admin):
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('code', 'name'), ('identificacion', 'telefono'),
            'direccion', 'activo')
        }),
    )
    list_display = ('code', 'name', 'identificacion',
        'telefono', 'direccion', 'activo')
    search_fields = ('code', 'name', 'identificacion')


admin.site.register(Factura, factura_admin)
admin.site.register(Proforma, factura_admin)
admin.site.register(Cliente, cliente_admin)