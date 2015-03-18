from moneycash.admin import documento_admin, \
model_empresa_admin as entidad_admin, admin
from .models import Compra, Proveedor, compra_detalle, Producto,\
Marca, Categoria
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form
import autocomplete_light


class producto_admin(entidad_admin):
    list_filter = ('marca', 'categoria')
    list_display = ('code', 'name', 'marca', 'categoria')
    fieldsets = (('Datos Generales', {'classes': ('grp-collapse grp-open',),
    'fields': (('code', 'name'), ('marca', 'categoria'))}),
        ('Datos de Comercializacion', {'classes': ('grp-collapse grp-open',),
            'fields': (('precio', 'costo'), ('descuento', 'existencias'),
                'activo')}))


class compra_detalle_tabular(admin.TabularInline):
    form = autocomplete_light.modelform_factory(compra_detalle)
    model = compra_detalle
    extra = 1
    fields = ('producto', 'cantidad', 'precio', 'descuento')
    classes = ('grp-collapse grp-open',)


class compra_admin(documento_admin, AjaxSelectAdmin):
    list_display = ('numero', 'fecha', 'proveedor',
        'subtotal', 'iva', 'total', 'ir', 'al', 'abonado', 'saldo',
        'fecha_vence')
    list_filter = ('periodo', 'user', 'proveedor', 'tipo')

    fieldsets = (
        ('Datos de La compra', {'classes': ('grp-collapse grp-open',),
            'fields': (('numero', 'fecha', 'moneda'),
                ('tipo', 'fecha_vence'), 'comentarios', 'proveedor',
                ('exento_iva', 'exento_ir', 'exento_al'))}),
        ("Detalle Inlines", {"classes":
            ("placeholder compra_detalle_set-group",), "fields": ()}),
        ('Impuestos y totales', {'classes': ('grp-collapse grp-open',),
            'fields': (('subtotal', 'ir'),
                        ('descuento', 'al'),
                        ('iva', ),
                        ('total', 'abonado', 'saldo'))}),
                )

    form = make_ajax_form(Compra, {'proveedor': 'proveedor'})
    inlines = [compra_detalle_tabular]
    readonly_fields = ('subtotal', 'descuento', 'iva',
    'ir', 'al', 'total', 'saldo')


#class compras_por_categoria(admin.TabularInline):
    #model = ComprasCategoria
    #fields = ('categoria', 'este_mes', 'este_anno', 'anno_anterior', 'total')
    #readonly_fields = fields
    #extra = 0


class proveedor_admin(entidad_admin):
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
        return super(proveedor_admin, self).response_change(request, obj)


admin.site.register(Proveedor, proveedor_admin)
admin.site.register(Compra, compra_admin)
admin.site.register(Producto, producto_admin)
admin.site.register(Marca, entidad_admin)
admin.site.register(Categoria, entidad_admin)

##usada unicamente para migracion
#from import_export.admin import ImportExportModelAdmin
#admin.site.register(compra_detalle, ImportExportModelAdmin)