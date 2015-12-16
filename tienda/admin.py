from django.contrib import admin
from .models import *


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'existencia')

admin.site.register(Articulo, ArticuloAdmin)
