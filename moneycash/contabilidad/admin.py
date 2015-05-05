from django.contrib import admin
from moneycash.admin import base_tabular
from import_export.admin import ImportExportModelAdmin
from .models import *
import autocomplete_light


class cuenta_tabular(base_tabular):
    model = Cuenta
    fields = ('code', 'name', 'saldo', 'saldo_actual')
    readonly_fields = ('saldo', 'saldo_actual')


class cuenta_admin(ImportExportModelAdmin):
    form = autocomplete_light.modelform_factory(Cuenta)
    list_display = ('code', 'name', 'saldo', 'saldo_actual', 'activo',
        'naturaleza')
    list_filter = ('activo', 'naturaleza')
    fieldsets = (('Datos de la Cuenta', {'classes': ('grp-collapse grp-open',),
    'fields': (('name', 'code', 'activo'), ('cuenta', 'naturaleza'),
    ('saldo', 'saldo_actual'))
    }),)
    ordering = ('code',)
    readonly_fields = ('saldo', 'saldo_actual')
    search_fields = ('code', 'name')
    inlines = [cuenta_tabular]


class cuentas_periodo(base_tabular):
    model = Balanza
    fields = ('cuenta', 'saldo_inicial', 'saldo_final')
    readonly_fields = ('cuenta', 'saldo_inicial', 'saldo_final')


class periodo_admin(admin.ModelAdmin):
    fields = (('fecha_inicial', 'fecha_final'), ('code', 'cerrado'))
    readonly_fields = ('code', 'cerrado')
    list_display = ('code', 'fecha_inicial', 'fecha_final', 'cerrado')
    inlines = [cuentas_periodo]
    actions = ['action_cerrar']

    def action_cerrar(self, request, queryset):
        for p in queryset:
            cerrar(p)
    action_cerrar.short_description = 'cerrar periodos seleccionadas'


class comprobante_movimientos(base_tabular):
    form = autocomplete_light.modelform_factory(Movimiento)
    model = Movimiento
    fields = ('cuenta', 'debe', 'haber')


class comprobante_admin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('numero', 'fecha', 'concepto', 'user')
    list_filter = ('periodo', 'user', 'sumas_iguales')
    search_fields = ('numero',)

    fieldsets = (('Datos Generales', {'classes': ('grp-collapse grp-open',),
    'fields': (('numero', 'fecha'), 'concepto')}),
        ("Detalle Inlines", {"classes":
            ("placeholder movimiento_set-group",), "fields": ()}),
        ('Totales', {'classes': ('grp-collapse grp-open',),
            'fields': (('sumas_iguales', 'total_debe', 'total_haber'),)}))

    readonly_fields = ('sumas_iguales', 'total_debe', 'total_haber')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    inlines = [comprobante_movimientos]


admin.site.register(Periodo, periodo_admin)
admin.site.register(Cuenta, cuenta_admin)
admin.site.register(Comprobante, comprobante_admin)
