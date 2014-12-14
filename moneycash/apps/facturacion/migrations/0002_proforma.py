# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0014_auto_20141213_1941'),
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proforma',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.factura',),
        ),
    ]
