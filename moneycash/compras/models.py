from moneycash.models import models, Provedor as base_provedor,\
Compra as base_compra, DetalleCompra as base_detalle,\
Item as base_producto, Marca as base_marca, Categoria as base_categoria
from moneycash.manager import Manager, empresa_manager
from moneycash.middlewares import get_current_user


class base(models.Model):
    objects = Manager()
    objects = empresa_manager()

    def save(self):
        self.empresa = get_current_user().empresa
        super(base, self).save()

    class Meta:
        abstract = True


class Producto(base, base_producto):
    class Meta:
        proxy = True


class Marca(base, base_marca):
    class Meta:
        proxy = True


class Categoria(base, base_categoria):
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
    provedor = models.ForeignKey(Provedor, blank=True)
    categoria = models.ForeignKey(Categoria, blank=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_categoria'
