# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0004_auto_20141218_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.compra',),
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.detallecompra',),
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.provedor',),
        ),
    ]
