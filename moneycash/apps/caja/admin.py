from moneycash.admin import admin
from moneycash.apps.caja.models import impresas,no_impresas

admin.site.register(impresas)
admin.site.register(no_impresas)