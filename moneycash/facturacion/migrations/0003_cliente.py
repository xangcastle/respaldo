# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0022_auto_20141215_1342'),
        ('facturacion', '0002_proforma'),
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
    ]
