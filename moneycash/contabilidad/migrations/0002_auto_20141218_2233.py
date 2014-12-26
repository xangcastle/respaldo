# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0004_auto_20141218_2158'),
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='costos_importacion',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.detallepoliza',),
        ),
        migrations.CreateModel(
            name='costos_internacion',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.detallepoliza',),
        ),
        migrations.CreateModel(
            name='costos_inventario',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.detallepoliza',),
        ),
        migrations.AlterModelOptions(
            name='poliza',
            options={'verbose_name_plural': 'liquidacion de polizas'},
        ),
    ]
