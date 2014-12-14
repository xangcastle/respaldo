# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0010_auto_20141213_1806'),
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
    ]
