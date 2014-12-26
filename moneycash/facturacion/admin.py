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
    fieldsets = (
        ('Datos Principales', {
        'classes': ('grp-collapse grp-open',),
        'fields': ('fecha', 'cliente')
        }),
        ("Detalle Inlines", {"classes":
            ("placeholder factura_detalle_set-group",), "fields": ()}),
        ('Opciones Adicionales', {'classes': ('grp-collapse grp-closed',),
            'fields': (('exento_iva', 'exento_iva_monto'),
                'alcaldia', 'retencion_ir')}),
        ('Datos calculados y Totales', {
        'classes': ('grp-collapse grp-open',),
        'fields': (('subtotal', 'descuento', 'iva', 'total'),
            ('retencion', 'costos', 'utilidad'),)
        }),
    )
    list_display = ('numero', 'fecha', 'cliente',
        'subtotal', 'descuento', 'total')
    inlines = [detalle_factura_tabular]
    form = make_ajax_form(Factura, {'cliente': 'cliente'})
    readonly_fields = ('subtotal', 'descuento', 'iva', 'total',
        'retencion', 'costos', 'utilidad')


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