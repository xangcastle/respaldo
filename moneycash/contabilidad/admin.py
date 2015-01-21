from moneycash.admin import admin, entidad_admin
from .models import Banco, Moneda, tipo_movimiento, Cuenta_Banco, tipo_cambio


admin.site.register(Banco, entidad_admin)
admin.site.register(Moneda, entidad_admin)
admin.site.register(tipo_movimiento, entidad_admin)
admin.site.register(Cuenta_Banco, entidad_admin)
admin.site.register(tipo_cambio)