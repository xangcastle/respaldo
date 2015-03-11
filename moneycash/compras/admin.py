from moneycash.admin import documento_admin, \
model_empresa_admin as entidad_admin, admin
from moneycash.compras.models import Compra, Provedor, DetalleCompra, Producto,\
Marca, Categoria # , ComprasCategoria
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form
import autocomplete_light
from import_export.admin import ImportExportModelAdmin


class producto_admin(entidad_admin):
    list_filter = ('marca', 'categoria')
    list_display = ('code', 'name', 'marca', 'categoria')


class compra_detalle(admin.TabularInline):
    form = autocomplete_light.modelform_factory(DetalleCompra)
    model = DetalleCompra
    extra = 1
    fields = ('item', 'cantidad', 'precio')
    classes = ('grp-collapse grp-open',)


class compra_admin(documento_admin, AjaxSelectAdmin):
    list_display = ('numero', 'fecha', 'provedor',
        'subtotal', 'iva', 'total', 'ir', 'al', 'abonado', 'saldo',
        'fecha_vence')
    list_filter = ('periodo', 'user', 'provedor', 'tipo')

    fieldsets = (
        ('Datos de La compra', {'classes': ('grp-collapse grp-open',),
            'fields': (('numero', 'fecha', 'moneda'),
                ('tipo', 'fecha_vence'), 'comentarios', 'provedor',
                ('exento_iva', 'exento_ir', 'exento_al'))}),
        ("Detalle Inlines", {"classes":
            ("placeholder detallecompra_set-group",), "fields": ()}),
        ('Impuestos y totales', {'classes': ('grp-collapse grp-open',),
            'fields': (('iva', 'ir', 'al', 'total'), ('abonado', 'saldo'),)}),
                )

    form = make_ajax_form(Compra, {'provedor': 'provedor'})
    inlines = [compra_detalle]
    readonly_fields = ('iva', 'ir', 'al', 'total', 'abonado', 'saldo')


#class compras_por_categoria(admin.TabularInline):
    #model = ComprasCategoria
    #fields = ('categoria', 'este_mes', 'este_anno', 'anno_anterior', 'total')
    #readonly_fields = fields
    #extra = 0


class provedor_admin(entidad_admin):
    list_display = ('code', 'name', 'identificacion', 'telefono',
        'limite_credito', 'tipo', 'total_compras', 'get_saldo')
    fields = ('name', ('code', 'identificacion'),
        ('telefono', 'tipo'), 'direccion',
        ('limite_credito', 'saldo', 'plazo'))
    list_filter = ('tipo',)
    #inlines = [compras_por_categoria]

    def response_change(self, request, obj):
        if '_popup' in request.REQUEST:
            request.path += '?_popup=1'
        return super(provedor_admin, self).response_change(request, obj)


class provedor_admin_IE(ImportExportModelAdmin, provedor_admin):
    # resouce_class = provedor_resource
    pass


class producto_admin_IE(ImportExportModelAdmin, producto_admin):
    # resouce_class = producto_resource
    pass


class entidad_admin_IE(ImportExportModelAdmin, entidad_admin):
    pass

admin.site.register(Provedor, provedor_admin_IE)
admin.site.register(Compra, compra_admin)
admin.site.register(Producto, producto_admin_IE)
admin.site.register(Marca, entidad_admin_IE)
admin.site.register(Categoria, entidad_admin_IE)