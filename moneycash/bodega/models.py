from moneycash.caja.models import models,impresa_manager, Factura as base_factura

class entregada_manager(impresa_manager):
    def get_queryset(self):
        return super(entregada_manager,self).get_queryset().filter(entregada=True)

class no_entregada_manager(impresa_manager):
    def get_queryset(self):
        return super(no_entregada_manager,self).get_queryset().filter(entregada=False)
    
class Factura(base_factura):
    objects = models.Manager()
    objects = entregada_manager()
    class Meta:
        proxy = True

class no_entregada(base_factura):
    objects = models.Manager()
    objects = no_entregada_manager()
    class Meta:
        proxy = True
        verbose_name = "factura"
        verbose_name_plural = "facturas pendientes"
