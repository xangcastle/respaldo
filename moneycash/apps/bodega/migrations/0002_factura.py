# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0002_auto_20141213_2353'),
        ('bodega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('caja.factura',),
        ),
    ]
