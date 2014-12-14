# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0009_factura_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='comentarios',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='costos',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura',
            name='descuento',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura',
            name='direccion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='iva',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura',
            name='nombre',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='numero',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='retencion',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura',
            name='subtotal',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura',
            name='telefono',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura',
            name='utilidad',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='costo_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='costo_unitario',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='descuento_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='descuento_unitario',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='precio_descontado',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='precio_descontado_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='precio_unitario',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='utilidad',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='costo',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='descuento',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='existencias',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]
