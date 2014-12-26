from moneycash.admin import documento_admin, entidad_admin, admin
from moneycash.compras.models import Compra, Provedor, Detalle
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline
from ajax_select import make_ajax_form


class compra_detalle(AjaxSelectAdminTabularInline):
    model = Detalle
    extra = 1
    fields = ('item', 'cantidad', 'precio')
    form = make_ajax_form(Detalle, {'item': 'item'})


class compra_admin(documento_admin, AjaxSelectAdmin):
    list_display = ('numero', 'fecha', 'provedor')
    list_filter = ('user', 'provedor')
    fieldsets = (
        ('Datos de La compra', {'classes': ('grp-collapse grp-open',),
            'fields': (('numero', 'fecha', 'moneda'), 'provedor')}),
        ("Detalle Inlines", {"classes":
            ("placeholder detalle_set-group",), "fields": ()}),
                )
    form = make_ajax_form(Compra, {'provedor': 'provedor'})
    inlines = [compra_detalle]


class provedor_admin(entidad_admin):
    fields = ('name', ('code', 'identificacion'), 'telefono', 'direccion',
        ('limite_credito', 'saldo'))

admin.site.register(Provedor, provedor_admin)
admin.site.register(Compra, compra_admin)
