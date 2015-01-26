from moneycash.models import models, Provedor as base_provedor,\
Compra as base_compra, DetalleCompra as base_detalle,\
Item as base_producto
from moneycash.manager import Manager, empresa_manager


class base(models.Model):
    objects = Manager()
    objects = empresa_manager()

    class Meta:
        abstract = True


class Producto(base, base_producto):
    class Meta:
        proxy = True


class Provedor(base, base_provedor):
    class Meta:
        proxy = True
        verbose_name_plural = "provedores"


class Compra(base, base_compra):
    class Meta:
        proxy = True


class Detalle(base, base_detalle):
    class Meta:
        proxy = True
        verbose_name = "producto"
        verbose_name_plural = "detalle de productos"


class ComprasCategoria(models.Model):
    provedor = models.ForeignKey(Provedor, blank=True, null=True)
    categoria = models.CharField(max_length=100, blank=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_categoria'
