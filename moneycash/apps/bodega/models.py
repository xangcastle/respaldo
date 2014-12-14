from moneycash.models import models, Factura as base_factura

class no_entregada_manager(models.Manager):
    def get_queryset(self):
        return super(no_entregada_manager,self).get_queryset().filter(autorizada=True,impresa=True,entregada=False)

class no_entregada(base_factura):
    objects = models.Manager()
    objects = no_entregada_manager()
    class Meta:
        proxy = True
        verbose_name = "factura"
        verbose_name_plural = "facturas pendientes"
