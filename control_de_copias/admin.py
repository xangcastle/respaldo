'''
Created on 20/09/2014

@author: abel
'''
from django.contrib import admin
from models import recibo
from recibos.admin import ReciboAdmin
class recibo_admin(ReciboAdmin):
    list_editable = ('contador_final',)
    actions = ['generar_imprimir']
    list_filter = ()
admin.site.register(recibo, recibo_admin)