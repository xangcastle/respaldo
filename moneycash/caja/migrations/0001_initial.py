# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0012_auto_20141213_1855'),
    ]

    operations = [
        migrations.CreateModel(
            name='impresas',
            fields=[
            ],
            options={
                'verbose_name': 'factura',
                'proxy': True,
                'verbose_name_plural': 'facturas impresas',
            },
            bases=('moneycash.factura',),
        ),
        migrations.CreateModel(
            name='no_impresas',
            fields=[
            ],
            options={
                'verbose_name': 'factura',
                'proxy': True,
                'verbose_name_plural': 'facturas no impresas',
            },
            bases=('moneycash.factura',),
        ),
    ]
