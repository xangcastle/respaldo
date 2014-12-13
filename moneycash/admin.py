from django.contrib import admin
from moneycash.models import Item, Marca, Categoria, Cliente, Factura,\
    factura_detalle, Periodo, Serie, Sucursal, Caja, Bodega

class base_admin(admin.ModelAdmin):
    list_display = ('code','name')
    actions = ['activar','inactivar']
    ordering = ('code',)
    def inactivar(self, request, queryset):
        queryset.update(activo=False)
    inactivar.short_description = "Deactivate selected objects"

    def activar(self, request, queryset):
        queryset.update(activo=True)
    activar.short_description = "Activate selected objects"

admin.site.register(Item,base_admin)
admin.site.register(Marca,base_admin)
admin.site.register(Categoria,base_admin)
admin.site.register(Cliente,base_admin)
admin.site.register(Factura)
admin.site.register(Periodo)
admin.site.register(Serie,base_admin)
admin.site.register(Sucursal,base_admin)
admin.site.register(Caja,base_admin)
admin.site.register(Bodega,base_admin)



