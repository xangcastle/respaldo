from moneycash.admin import admin, factura_admin as base_factura_admin
from moneycash.apps.facturacion.models import Factura

class factura_admin(base_factura_admin):
    pass

admin.site.register(Factura, factura_admin)
