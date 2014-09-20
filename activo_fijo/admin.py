'''
Created on 20/09/2014

@author: abel
'''
from django.contrib import admin
from recibos.admin import EquipoAdmin,MarcaAdmin
from models import equipo,marca
admin.site.register(equipo, EquipoAdmin)
admin.site.register(marca, MarcaAdmin)