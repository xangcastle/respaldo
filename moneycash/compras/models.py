from moneycash.models import Provedor as base_provedor, Compra as base_compra,\
DetalleCompra as base_detalle


class Provedor(base_provedor):
    class Meta:
        proxy = True
        verbose_name_plural = "provedores"


class Compra(base_compra):
    class Meta:
        proxy = True


class Detalle(base_detalle):
    class Meta:
        proxy = True
