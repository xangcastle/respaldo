from moneycash.models import models, Factura as base_factura

class proforma_manager(models.Manager):
    def get_queryset(self):
        return super(proforma_manager,self).get_queryset().filter(autorizada=False)

class factura_manager(models.Manager):
    def get_queryset(self):
        return super(factura_manager,self).get_queryset().filter(autorizada=True)


class Factura(base_factura):
    objects = models.Manager()
    objects = factura_manager()
    class Meta:
        proxy = True
        
class Proforma(base_factura):
    objects = models.Manager()
    objects = proforma_manager()
    class Meta:
        proxy = True