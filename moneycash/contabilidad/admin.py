from moneycash.admin import admin, entidad_admin
from .models import Banco, Moneda


admin.site.register(Banco, entidad_admin)
admin.site.register(Moneda, entidad_admin)