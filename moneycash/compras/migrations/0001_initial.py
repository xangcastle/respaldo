# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('este_mes', models.FloatField(null=True, blank=True)),
                ('este_anno', models.FloatField(null=True, blank=True)),
                ('anno_anterior', models.FloatField(null=True, blank=True)),
                ('total', models.FloatField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'db_table': 'compras_categoria',
                'managed': False,
                'verbose_name_plural': 'compras por categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.categoria',),
        ),
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
            name='DetalleCompra',
            fields=[
            ],
            options={
                'verbose_name': 'producto',
                'proxy': True,
                'verbose_name_plural': 'detalle de productos',
            },
            bases=('moneycash.detallecompra',),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.marca',),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.item',),
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
            ],
            options={
                'verbose_name': 'proveedor',
                'proxy': True,
                'verbose_name_plural': 'proveedores',
            },
            bases=('moneycash.provedor',),
        ),
    ]
