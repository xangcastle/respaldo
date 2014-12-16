# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.cliente',),
        ),
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
            name='Proforma',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.factura',),
        ),
    ]
