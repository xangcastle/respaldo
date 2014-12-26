# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0006_auto_20141219_0214'),
        ('contabilidad', '0002_auto_20141218_2233'),
    ]

    operations = [
        migrations.DeleteModel(
            name='costos_importacion',
        ),
        migrations.DeleteModel(
            name='costos_internacion',
        ),
        migrations.DeleteModel(
            name='costos_inventario',
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'facturas incluidas en la poliza',
            },
            bases=('moneycash.detallepoliza',),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'productos incluidos en la poliza',
            },
            bases=('moneycash.poliza_producto',),
        ),
    ]
