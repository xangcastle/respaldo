'''
Created on 20/09/2014

@author: abel
'''
from django.contrib import admin
from models import recibo
class recibo_admin(admin.ModelAdmin):
    list_display = ('area','equipo','contador_inicial','contador_final','total_copias','copia_diferencia')
    list_editable = ('contador_inicial','contador_final')
admin.site.register(recibo, recibo_admin)