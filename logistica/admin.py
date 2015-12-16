from django.contrib import admin
from metropolitana.admin import entidad_admin
from .models import *


class municipio_admin(entidad_admin):
    list_display = ('code', 'name')


class barrio_admin(entidad_admin):
    list_display = ('code', 'name', 'departamento', 'municipio')
    list_filter = ('departamento', 'municipio')


admin.site.register(Barrio, entidad_admin)
admin.site.register(Municipio, municipio_admin)
admin.site.register(Departamento, entidad_admin)
