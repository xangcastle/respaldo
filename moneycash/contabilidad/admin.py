from moneycash.admin import admin, documento_admin
from moneycash.contabilidad.models import Poliza, Factura#, Producto


class poliza_factura(admin.TabularInline):
    model = Factura


#class poliza_producto(admin.TabularInline):
    #model = Producto


class poliza_admin(documento_admin):
    #inlines = [poliza_factura, poliza_producto]
    pass


admin.site.register(Poliza, poliza_admin)
