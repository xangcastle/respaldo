'''
Created on 20/09/2014

@author: abel
'''
from django.contrib import admin
from models import produccion_equipo
from recibos.admin import ReciboAdmin
class produccion_equipo_admin(ReciboAdmin):
    list_editable = ('contador_final',)
    actions = ['generar_imprimir']
    list_filter = ()
admin.site.register(produccion_equipo, produccion_equipo_admin)