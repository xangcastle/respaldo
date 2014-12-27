# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0012_auto_20141227_0031'),
        ('compras', '0003_auto_20141226_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.item',),
        ),
    ]
