from django.contrib import admin
from .models import *
from moneycash.admin import entidad_admin

admin.site.register(Usuario, entidad_admin)
admin.site.register(Grupo, entidad_admin)
admin.site.register(Agencia, entidad_admin)
