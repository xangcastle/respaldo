# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.compra', models.Model),
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
            ],
            options={
                'verbose_name': 'producto',
                'proxy': True,
                'verbose_name_plural': 'detalle de productos',
            },
            bases=('moneycash.detallecompra', models.Model),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.item', models.Model),
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'provedores',
            },
            bases=('moneycash.provedor', models.Model),
        ),
        migrations.CreateModel(
            name='ComprasCategoria',
            fields=[
            ],
            options={
                'db_table': 'compras_categoria',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
