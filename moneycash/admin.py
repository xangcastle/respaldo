from django.contrib import admin
from moneycash.models import Item, Marca, Categoria, Cliente, Factura,\
    factura_detalle, Periodo, Serie, Sucursal, Caja


admin.site.register(Item)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(factura_detalle)
admin.site.register(Periodo)
admin.site.register(Serie)
admin.site.register(Sucursal)
admin.site.register(Caja)



