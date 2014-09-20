'''
Created on 20/09/2014

@author: abel
'''
from django.contrib import admin
from models import recibo
from recibos.admin import ReciboAdmin
from django.shortcuts import render_to_response
from django.template.context import RequestContext
class recibo_admin(admin.ModelAdmin):
    list_display = ReciboAdmin.list_display
    list_editable = ReciboAdmin.list_editable
    actions = ['generar_imprimir']
    def generar_imprimir(self, request, queryset):
        id_unico = False
        if queryset.count() == 1:
            id_unico = True
        ctx = {'queryset':queryset,'id_unico':id_unico}
        return render_to_response('recibos/impreso.html',ctx,context_instance=RequestContext(request))
    generar_imprimir.short_description = "Imprimir recibos selecionados"
admin.site.register(recibo, recibo_admin)