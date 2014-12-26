from moneycash.models import models, Factura as base_factura
from moneycash.manager import documento_no_entregado, documento_entregado


class Factura(base_factura):
    objects = models.Manager()
    objects = documento_entregado()

    class Meta:
        proxy = True


class no_entregada(base_factura):
    objects = models.Manager()
    objects = documento_no_entregado()

    class Meta:
        proxy = True
        verbose_name = "factura"
        verbose_name_plural = "facturas pendientes"
