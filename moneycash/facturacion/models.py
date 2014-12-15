from moneycash.models import models, Factura as base_factura
from moneycash.manager import documento_no_autorizado, documento_autorizado

class Proforma(base_factura):
    objects = models.Manager()
    objects = documento_no_autorizado()
    class Meta:
        proxy = True

class Factura(base_factura):
    objects = models.Manager()
    objects = documento_autorizado()
    class Meta:
        proxy = True
        
