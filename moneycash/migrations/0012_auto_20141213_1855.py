# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0011_auto_20141213_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura_detalle',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos y/o servicios'},
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='codigo',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura',
            name='alcaldia',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='factura',
            name='exento_iva',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='factura',
            name='exento_iva_monto',
            field=models.FloatField(null=True, verbose_name=b'porcentaje autorizado por la dgi', blank=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='retencion_ir',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='categoria',
            field=models.ForeignKey(blank=True, to='moneycash.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='item',
            field=models.ForeignKey(blank=True, to='moneycash.Item', null=True),
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='marca',
            field=models.ForeignKey(blank=True, to='moneycash.Marca', null=True),
        ),
    ]
