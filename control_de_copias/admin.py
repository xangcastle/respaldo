'''
Created on 20/09/2014

@author: abel
'''
from django.contrib import admin
from models import recibo
from recibos.admin import ReciboAdmin
class recibo_admin(admin.ModelAdmin):
    list_display = ReciboAdmin.list_display
    list_editable = ReciboAdmin.list_editable
    actions = [ReciboAdmin.generar_imprimir]
admin.site.register(recibo, recibo_admin)