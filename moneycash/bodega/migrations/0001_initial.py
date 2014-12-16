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
            },
            bases=('moneycash.factura',),
        ),
        migrations.CreateModel(
            name='no_entregada',
            fields=[
            ],
            options={
                'verbose_name': 'factura',
                'proxy': True,
                'verbose_name_plural': 'facturas pendientes',
            },
            bases=('moneycash.factura',),
        ),
    ]
