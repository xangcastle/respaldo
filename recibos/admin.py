from django.contrib import admin
from django.contrib.admin import site
from recibos.models import Area, Equipo, Periodo, Recibo, Detalle, Ubicacion,\
Marca, Requisa, DetalleRequisa, Articulo
from import_export.admin import ImportExportModelAdmin
from django.template.context import RequestContext
from django.shortcuts import render_to_response
import adminactions.actions as actions
from totalsum.admin import TotalsumAdmin

actions.add_to_site(site)


class DetalleInlines(admin.TabularInline):
    model = Detalle
    extra = 0
    classes = ('grp-collapse grp-closed',)


class Equipoinline(admin.TabularInline):
    model = Equipo


class Areainline(admin.TabularInline):
    model = Area


class Reciboinline(admin.TabularInline):
    model = Recibo


class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'responsable', 'codigo', 'equipo', 'direccion')
    list_filter = ('codigo', 'ubicacion')
    ordering = ('nombre', 'responsable', 'codigo')
    search_fields = ('nombre', 'responsable')


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'nombre_area', 'contador', 'costo', 'vida_util',
    'valor_de_depreciacion', 'comentarios', 'valor_actual', 'activo')
    list_filter = ('ubicacion', 'activo')
    search_fields = ('modelo', 'serie')
    list_editable = ('contador', 'costo', 'vida_util')


class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion')
    ordering = ('nombre',)
    #inlines = [Areainline]


class ReciboAdmin(TotalsumAdmin):
    fieldsets = (
        ('Datos Generales', {
            'classes': ('grp-collapse grp-open',),
            'fields': (('periodo', 'equipo'),)
        }),
        ('Contadores y Meta', {
            'fields': (('contador_inicial', 'contador_final', 'meta'),)
        }),

        ('Datos de Facturacion', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (('precio_copia', 'tasa_cambio'),)
        }),
        ('Costos de Produccion', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (('costo_papel', 'costo_partes'),
                ('costo_administrativo', 'depreciacion_activo'),)
        }),
    )
    list_display = ('area', 'equipo', 'contador_inicial', 'contador_final',
        'total_copias', 'costo_partes', 'costo_papel', 'costo_administrativo',
        'depreciacion_activo', 'meta', 'cumplimiento')
    list_filter = ('periodo', 'equipo')
    ordering = ('-periodo',)
    inlines = [DetalleInlines]
    list_editable = ('contador_inicial', 'contador_final', 'costo_partes',
        'costo_papel', 'costo_administrativo', 'depreciacion_activo', 'meta')
    totalsum_list = ('costo_partes')

    actions = ['generar_imprimir']

    def generar_imprimir(self, request, queryset):
        id_unico = False
        if queryset.count() == 1:
            id_unico = True
        ctx = {'queryset': queryset, 'id_unico': id_unico}
        return render_to_response('recibos/impreso.html', ctx,
            context_instance=RequestContext(request))
    generar_imprimir.short_description = "Imprimir recibos selecionados"


class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'equipo', 'tecnico', 'contador')


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    inlines = [Equipoinline]


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicial', 'fecha_final', 'total_copias',
        'total_dolares', 'total_costos', 'utilidad_total', 'cuadro', 'cerrado')
    list_filter = ('fecha_final', 'cerrado')
    #totalsum_list = ('total_copias',)

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.generar_recibos()
        if obj.cerrado:
            obj.cerrar()


class Item_admin(ImportExportModelAdmin, admin.ModelAdmin):
    # resouce_class = Item_resouce
    list_display = ('no_parte', 'nombre', 'duracion', 'costo')
    search_fields = ('no_parte', 'nombre')


class detalle_requisa_tabular(admin.StackedInline):
    model = DetalleRequisa
    extra = 0
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class RequisaAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha'
    list_display = ('numero_requisa', 'fecha', 'site_origen',
        'site_destino', 'tipo_requisa', 'str_detalle', 'costo_total')
    list_filter = ('periodo', 'tipo_requisa', 'site_origen', 'site_destino')
    search_fields = ('id',)
    inlines = [detalle_requisa_tabular]
    actions = ['imprimir_requisa']

    def imprimir_requisa(self, request, queryset):
        id_unico = False
        if queryset.count() == 1:
            id_unico = True
        ctx = {'queryset': queryset, 'id_unico': id_unico}
        return render_to_response('recibos/requisa.html', ctx,
            context_instance=RequestContext(request))
    imprimir_requisa.short_description = "Imprimir requisas selecionadas"


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'marca', 'costo', 'total_entradas',
        'total_salidas', 'existencias', 'inventario')


class SiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Area, AreaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Recibo, ReciboAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Requisa, RequisaAdmin)
admin.site.register(Articulo, ArticuloAdmin)
#admin.site.register(Site, SiteAdmin)


