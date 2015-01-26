# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_auto_20150125_2307'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.categoria', models.Model),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.marca', models.Model),
        ),
    ]
