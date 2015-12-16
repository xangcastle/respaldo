from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


class producto_admin(ImportExportModelAdmin):
    list_display = ('codigo', 'descripcion', 'marca', 'rack', 'columna', 'fila',
        'costo', 'existencia', 'conteo1', 'conteo2', 'conteo3')
    list_filter = ('rack', 'con_diferencia')

admin.site.register(Producto, producto_admin)