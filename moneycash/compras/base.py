# -*- coding: utf-8 -*-
from moneycash.base import models, EmpresaModel


class base_item(EmpresaModel):
    marca = models.ForeignKey('Marca', null=True, blank=True)
    categoria = models.ForeignKey('Categoria', null=True, blank=True)
    existencias = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    class Meta:
        abstract = True


class base_detalle_compra(models.Model):

    compra = models.ForeignKey('Compra', null=True, blank=True)
    item = models.ForeignKey('Item')
    cantidad = models.FloatField(default=1)
    precio = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    costo = models.FloatField(default=0)
    existencias = models.FloatField(default=0)
    costo_promedio = models.FloatField(default=0)
    costo_importacion = models.FloatField(default=0)
    costo_internacion = models.FloatField(default=0)
    recibido = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return str(self.item)

    class Meta:
        abstract = True
        verbose_name = "producto"