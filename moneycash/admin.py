from django.contrib import admin
from .models import Periodo, Sucursal, Caja, Bodega, Pago, Banco,\
Moneda, TipoCosto, CierreCaja, Empresa, Factura
from django.contrib.auth.admin import UserAdmin as base_useradmin


class user_admin(base_useradmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
        'is_staff', 'empresa')
    list_editable = ('empresa', )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'empresa')

#admin.site.register(User, user_admin)


class entidad_admin(admin.ModelAdmin):
    list_display = ('code', 'name')
    actions = ['activar', 'inactivar']
    ordering = ('code',)
    search_fields = ('code', 'name')
    ordering = ('name',)

    def inactivar(self, request, queryset):
        queryset.update(activo=False)
    inactivar.short_description = "Deactivate selected objects"

    def activar(self, request, queryset):
        queryset.update(activo=True)
    activar.short_description = "Activate selected objects"


class model_empresa_admin(entidad_admin):
    exclude = ('empresa',)


class documento_admin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('numero', 'fecha', 'user', 'sucursal',
        'impreso', 'entregado', 'contabilizado')
    list_filter = ('periodo', 'user', 'sucursal', 'impreso',
        'entregado', 'contabilizado')
    search_fields = ('numero',)

    def save_model(self, request, obj, form, change):
        super(documento_admin, self).save_model(request, obj, form, change)
        obj.user = request.user
        obj.periodo = Periodo.objects.get(fecha_inicial__lte=obj.fecha,
        fecha_final__gte=obj.fecha)
        obj.save()


class documento_caja_admin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super(documento_admin, self).save_model()
        obj.cierre_caja = CierreCaja.objects.get(fecha_inicial__lte=self.fecha,
            fecha_final__gte=self.fecha)
        obj.save()


class periodo_admin(admin.ModelAdmin):
    list_display = ('fecha_inicial', 'fecha_final', 'iva_pagado',
        'ir_cobrado', 'cerrado')


admin.site.register(Periodo, periodo_admin)
admin.site.register(Sucursal, entidad_admin)
admin.site.register(Caja, entidad_admin)
admin.site.register(Bodega, entidad_admin)
admin.site.register(Pago, entidad_admin)
admin.site.register(Banco, entidad_admin)
admin.site.register(Moneda, entidad_admin)
admin.site.register(TipoCosto, entidad_admin)
admin.site.register(Empresa, entidad_admin)
admin.site.register(Factura, documento_admin)