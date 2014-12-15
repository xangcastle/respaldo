from moneycash.admin import documento_admin
from moneycash.facturacion.admin import admin,factura_admin
from moneycash.bodega.models import no_entregada, Factura

class no_entragada_admin(documento_admin):
    pass

admin.site.register(Factura,factura_admin)
admin.site.register(no_entregada,no_entragada_admin)