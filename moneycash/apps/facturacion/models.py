from moneycash.models import Factura as base_factura

class Factura(base_factura):
    class Meta:
        proxy = True