from moneycash.apps.facturacion.admin import admin,factura_admin
from moneycash.apps.bodega.models import no_entregada, Factura

admin.site.register(Factura,factura_admin)
admin.site.register(no_entregada)