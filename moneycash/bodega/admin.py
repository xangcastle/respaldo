from moneycash.facturacion.admin import admin,factura_admin
from moneycash.bodega.models import no_entregada, Factura

admin.site.register(Factura,factura_admin)
admin.site.register(no_entregada)