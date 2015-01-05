# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
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
            name='Poliza',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'liquidacion de polizas',
            },
            bases=('moneycash.poliza',),
        ),
    ]
