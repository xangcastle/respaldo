from moneycash.admin import admin, entidad_admin
from .models import Banco


class banco_admin(entidad_admin):
    pass


admin.site.register(Banco, banco_admin)