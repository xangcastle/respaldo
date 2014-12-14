from moneycash.models import models, Factura as base_factura

class impresa_manager(models.Manager):
    def get_queryset(self):
        return super(impresa_manager,self).get_queryset().filter(autorizada=True,impresa=True)
    
class no_impresa_manager(models.Manager):
    def get_queryset(self):
        return super(no_impresa_manager,self).get_queryset().filter(autorizada=True,impresa=False)

class impresas(base_factura):
    objects = models.Manager()
    objects = impresa_manager()
    class Meta:
        proxy = True
        verbose_name = "factura"
        verbose_name_plural = "facturas impresas"
        
class no_impresas(base_factura):
    objects = models.Manager()
    objects = no_impresa_manager()
    class Meta:
        proxy = True
        verbose_name = "factura"
        verbose_name_plural = "facturas no impresas"
