from moneycash.models import models, Provedor as base_provedor,\
Marca as base_marca, Categoria as base_categoria, \
DetalleCompra as base_detalle_compra, Item as base_item, \
Compra as base_compra


class Item(base_item):
    class Meta:
        proxy = True


class Marca(base_marca):
    class Meta:
        proxy = True


class Categoria(base_categoria):
    class Meta:
        proxy = True


class Provedor(base_provedor):
    class Meta:
        proxy = True
        verbose_name_plural = "provedores"


class Compra(base_compra):
    class Meta:
        proxy = True


class DetalleCompra(base_detalle_compra):
    class Meta:
        proxy = True
        verbose_name = "producto"
        verbose_name_plural = "detalle de productos"


class ComprasCategoria(models.Model):
    provedor = models.ForeignKey(Provedor, blank=True)
    categoria = models.ForeignKey(Categoria, blank=True)
    este_mes = models.FloatField(blank=True, null=True)
    este_anno = models.FloatField(blank=True, null=True)
    anno_anterior = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compras_categoria'
        verbose_name = "categoria"
        verbose_name_plural = "compras por categorias"
