from django.contrib import admin
from django.contrib.admin import site
import adminactions.actions as actions
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import *
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from .views import *

actions.add_to_site(site)


class entidad_admin(ImportExportModelAdmin):
    list_display = ('code', 'name')
    #actions = ['activar', 'inactivar']
    ordering = ('code',)
    search_fields = ('code', 'name')
    ordering = ('name',)

    def inactivar(self, request, queryset):
        queryset.update(activo=False)
    inactivar.short_description = "Deactivate selected objects"

    def activar(self, request, queryset):
        queryset.update(activo=True)
    activar.short_description = "Activate selected objects"


class control_entregas_admin(entidad_admin):
    list_display = ('code', 'name', 'pendientes', 'asignados', 'entregados')
    readonly_fields = ('pendientes', 'asignados', 'entregados')
    actions = ['actualizar_estadisticas_entrega']

    def actualizar_estadisticas_entrega(self, request, queryset):
        actualizar_estadisticas_entrega(queryset)
    actualizar_estadisticas_entrega.short_description = \
    "Actualizar estadisticas de entregas"


class base_tabular(admin.TabularInline):
    classes = ('grp-collapse grp-open',)
    extra = 0


class paquete_admin(ImportExportModelAdmin):
    resouce_class = paquete_resouce
    search_fields = ('factura', 'contrato', 'cliente', 'barra')
    list_display = ('factura', 'contrato', 'cliente', 'departamento',
        'municipio', 'barrio', 'direccion', 'servicio', 'entrega',
        'ciclo', 'mes', 'ano', 'link_comprobante')
    list_filter = ('departamento', 'municipio', 'lotificado', 'entrega',
        'ciclo', 'mes', 'ano')

    fieldsets = (('Datos Generales', {'classes': ('grp-collapse grp-open',),
    'fields': (('factura', 'cliente', 'contrato'), ('ciclo', 'mes', 'ano'),
    ('departamento', 'municipio', 'barrio'), ('direccion', 'lote'),
    ('telefono_contacto', 'ruta', 'zona'))}),
        ('Datos de Facturacion', {'classes': ('grp-collapse grp-open',),
            'fields': (('segmento', 'tarifa', 'servicio'),
                ('cupon', 'total_mes_factura', 'valor_pagar'),
                ('numero_fiscal', 'factura_interna', 'entrega'))}))

    readonly_fields = ('factura', 'cliente', 'contrato', 'cupon', 'ciclo',
        'mes', 'ano', 'departamento', 'municipio', 'barrio', 'direccion',
        'telefono_contacto', 'ruta', 'zona', 'segmento', 'tarifa', 'servicio',
        'cupon', 'total_mes_factura', 'valor_pagar', 'numero_fiscal',
        'factura_interna', 'entrega', 'lote')
    actions = ['action_lotificar']

    change_list_template = 'admin/metropolitana/paquete/change_list.html'

    def action_lotificar(self, request, queryset):
        lotificar(queryset)
    action_lotificar.short_description = 'lotificar facturas seleccionadas'


class municipio_admin(entidad_admin):
    list_display = ('code', 'name', 'departamento')
    list_filter = ('departamento', )


class barrio_admin(entidad_admin):
    list_display = ('code', 'name', 'departamento', 'municipio')
    list_filter = ('departamento', 'municipio')


class cliente_admin(entidad_admin):
    list_display = ('contrato', 'name', 'departamento', 'municipio', 'barrio',
        'direccion', 'telefono_contacto', 'valor_pagar')
    list_filter = ('departamento', 'municipio', 'barrio', 'segmento', 'tarifa',
        'servicio')


class facturas_asignadas(base_tabular):
    model = Paquete
    fields = ('consecutivo', 'factura', 'cliente', 'direccion',
        'telefono_contacto', 'comprobante')
    readonly_fields = ('factura', 'cliente', 'direccion',
        'telefono_contacto')
    sortable_field_name = 'consecutivo'
    #sortable_excludes = ('telefono_contacto', 'comprobante', 'consecutivo')


class lote_admin(ImportExportModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('numero', 'municipio', 'departamento', 'barrio',
        'cerrado', 'cantidad_paquetes', 'entregados', 'avance', 'asignado',
        'colector', 'ciclo', 'mes', 'ano')
    list_filter = ('municipio', 'departamento', 'asignado', 'colector',
        'ciclo', 'mes', 'ano')

    fieldsets = (
        ('Datos del Lote', {'classes': ('grp-collapse grp-open',),
            'fields': (('numero', 'colector'), ('municipio', 'departamento'),
                'barrio', ('cantidad_paquetes', 'entregados', 'avance'))}),
                )

    readonly_fields = ('numero', 'municipio', 'departamento', 'barrio',
        'cantidad_paquetes', 'entregados', 'avance')
    inlines = [facturas_asignadas]
    actions = ['generar_comprobantes']

    #list_editable = ('comprobantes',)

    def generar_comprobantes(self, request, queryset):
        id_unico = False
        if queryset.count() == 1:
            id_unico = True
        ctx = {'queryset': queryset, 'id_unico': id_unico}
        return render_to_response('metropolitana/comprobante.html',
            ctx, context_instance=RequestContext(request))
    generar_comprobantes.short_description = \
    "Generar comprobantes de los lotes selecionados"


admin.site.register(Paquete, paquete_admin)
admin.site.register(Colector, control_entregas_admin)
admin.site.register(Departamento, control_entregas_admin)
admin.site.register(Municipio, control_entregas_admin)
admin.site.register(Barrio, barrio_admin)
admin.site.register(Cliente, cliente_admin)
admin.site.register(Lote, lote_admin)

