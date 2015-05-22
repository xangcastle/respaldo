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
import math

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
    list_display = ('code', 'name', 'asignados', 'entregados', 'pendientes')
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
                ('numero_fiscal', 'factura_interna', 'entrega'))}),
        ('Entrega y Digitalizacion', {'classes': ('grp-collapse grp-open',),
            'fields': (('comprobante', 'colector'),)}))

    readonly_fields = ('factura', 'cliente', 'contrato', 'cupon', 'ciclo',
        'mes', 'ano', 'departamento', 'municipio', 'barrio', 'direccion',
        'telefono_contacto', 'ruta', 'zona', 'segmento', 'tarifa', 'servicio',
        'cupon', 'total_mes_factura', 'valor_pagar', 'numero_fiscal',
        'factura_interna', 'entrega', 'lote', 'colector')
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
    fields = ('factura', 'cliente', 'comprobante', 'direccion',
        'telefono_contacto')
    readonly_fields = ('factura', 'cliente', 'direccion',
        'telefono_contacto')
    #sortable_field_name = 'consecutivo'


class lote_admin(ImportExportModelAdmin):
    date_hierarchy = 'fecha'
    search_fields = ('numero', 'colector__name', 'departamento__name',
        )
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
    actions = ['generar_comprobantes', 'ordenar_cliente', 'ordenar_direccion']

    def generar_comprobantes(self, request, queryset):
        paginas = []
        id_unico = False
        if queryset.count() == 1:
            id_unico = True
        comprobantes = Paquete.objects.filter(
            lote__in=queryset).order_by('lote', 'consecutivo')
        if comprobantes:
            pagina = {'comprobantes': []}
            for c in comprobantes:
                pagina['comprobantes'].append(c)
                if len(pagina['comprobantes']) == 4:
                    paginas.append(pagina)
                    pagina = {'comprobantes': []}
            if len(pagina['comprobantes']) > 0:
                paginas.append(pagina)
        ctx = {'queryset': queryset, 'id_unico': id_unico, 'paginas': paginas}
        return render_to_response('metropolitana/comprobante.html',
            ctx, context_instance=RequestContext(request))
    generar_comprobantes.short_description = \
    "Generar comprobantes de los lotes selecionados"

    def ordenar_cliente(self, request, queryset):
        for p in queryset:
            p.ordenar_por_cliente()
    ordenar_cliente.short_description = 'ordenar paquetes por cliente'

    def ordenar_direccion(self, request, queryset):
        for p in queryset:
            p.ordenar_por_direccion()
    ordenar_direccion.short_description = 'ordenar paquetes por direccion'


class impresion_admin(ImportExportModelAdmin):
    date_hierarchy = 'fecha_verificacion'
    list_display = ('consecutivo', 'paquete', 'cliente', 'user', 'fecha_verificacion')
    list_filter = ('user',)
    search_fields = ('paquete__cliente', 'paquete__factura', 'paquete__barra',
        'paquete__contrato')
    actions = ['generar_comprobantes']

    def generar_comprobantes(self, request, queryset):
        paginas = []
        id_unico = False
        if queryset.count() == 1:
            id_unico = True
        for q in queryset:
            c = Paquete.objects.get(id=q.paquete.id)
            c.orden_impresion = q.consecutivo
            c.save()
        comprobantes = Paquete.objects.filter(
            id__in=queryset.order_by('consecutivo').values_list('paquete',
                flat=True)).order_by('orden_impresion')
        if comprobantes:
            pagina = {'comprobantes': []}
            for c in comprobantes:
                pagina['comprobantes'].append(c)
                if len(pagina['comprobantes']) == 4:
                    paginas.append(pagina)
                    pagina = {'comprobantes': []}
            if len(pagina['comprobantes']) > 0:
                paginas.append(pagina)
        ctx = {'queryset': queryset, 'id_unico': id_unico, 'paginas': paginas}
        return render_to_response('metropolitana/comprobante.html',
            ctx, context_instance=RequestContext(request))
    generar_comprobantes.short_description = \
    "Generar comprobantes selecionados"


admin.site.register(Paquete, paquete_admin)
admin.site.register(Colector, control_entregas_admin)
admin.site.register(Departamento, control_entregas_admin)
admin.site.register(Municipio, control_entregas_admin)
admin.site.register(Barrio, barrio_admin)
admin.site.register(Cliente, cliente_admin)
admin.site.register(Lote, lote_admin)
admin.site.register(impresion, impresion_admin)


       #If ch.Cuenta.Producto.Formato.Codigo = 2 Then
            #For bucle = 1 To CInt(ch.cantidad / ch.Cuenta.Producto.Plana.ChequesxPagina)
                #For index = bucle - 1 To (ch.cantidad - 1) Step CInt(ch.cantidad / ch.Cuenta.Producto.Plana.ChequesxPagina)
                    #tb.Rows.Add(lc(index).agencia, lc(index).ruta, lc(index).cuenta, lc(index).cheque, lc(index).moneda, lc(index).barra, lc(index).nombre, lc(index).nombreAd, lc(index).direccion1, lc(index).direccion2, lc(index).direccion3, lc(index).direccion4, lc(index).telefono, Imagen_Bytes(lc(index).logoProducto), Imagen_Bytes(lc(index).logoCliente))
                #Next
            #Next
        #Else


        #for a in range(1, total, cantidadxpagina):
            #for


#def cantidad_paginas(total):
    #if