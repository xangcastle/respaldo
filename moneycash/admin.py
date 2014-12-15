from django.contrib import admin
from moneycash.models import Item, Marca, Categoria, Cliente,\
    Periodo, Serie, Sucursal, Caja, Bodega, Pago, Banco, Moneda

class entidad_admin(admin.ModelAdmin):
    list_display = ('code','name')
    actions = ['activar','inactivar']
    ordering = ('code',)
    
    def inactivar(self, request, queryset):
        queryset.update(activo=False)
    inactivar.short_description = "Deactivate selected objects"

    def activar(self, request, queryset):
        queryset.update(activo=True)
    activar.short_description = "Activate selected objects"
    
class documento_admin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.periodo = Periodo.objects.get(fecha_inicial__lte=self.fecha,fecha_final__gte=self.fecha)
        obj.user = request.user
        obj.save()
    
admin.site.register(Item,entidad_admin)
admin.site.register(Marca,entidad_admin)
admin.site.register(Categoria,entidad_admin)
admin.site.register(Cliente,entidad_admin)
admin.site.register(Periodo)
admin.site.register(Serie,entidad_admin)
admin.site.register(Sucursal,entidad_admin)
admin.site.register(Caja,entidad_admin)
admin.site.register(Bodega,entidad_admin)
admin.site.register(Pago,entidad_admin)
admin.site.register(Banco,entidad_admin)
admin.site.register(Moneda,entidad_admin)




