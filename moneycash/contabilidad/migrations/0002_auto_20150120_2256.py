# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0007_tipo_movimiento'),
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='Poliza',
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.banco',),
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.moneda',),
        ),
        migrations.CreateModel(
            name='tipo_movimiento',
            fields=[
            ],
            options={
                'verbose_name': 'tipo de transaccion',
                'proxy': True,
                'verbose_name_plural': 'tipos de transacciones',
            },
            bases=('moneycash.tipo_movimiento',),
        ),
    ]
