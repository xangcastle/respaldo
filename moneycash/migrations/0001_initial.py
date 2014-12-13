# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import moneycash.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('bodegas', models.ManyToManyField(to='moneycash.Bodega')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('comentarios', models.CharField(max_length=200)),
                ('exento_iva', models.BooleanField(default=True)),
                ('exento_iva_monto', models.FloatField(null=True, blank=True)),
                ('alcaldia', models.BooleanField(default=True)),
                ('retencion_ir', models.BooleanField(default=True)),
                ('subtotal', models.FloatField()),
                ('descuento', models.FloatField()),
                ('iva', models.FloatField()),
                ('total', models.FloatField()),
                ('retencion', models.FloatField()),
                ('costos', models.FloatField()),
                ('utilidad', models.FloatField()),
                ('impresa', models.BooleanField(default=True)),
                ('contabilizada', models.BooleanField(default=True)),
                ('autorizada', models.BooleanField(default=True)),
                ('vendedor', models.FloatField(verbose_name=django.contrib.auth.models.User)),
                ('sucursal', models.FloatField(verbose_name=moneycash.models.Sucursal)),
                ('cliente', models.ForeignKey(to='moneycash.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='factura_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField()),
                ('descuento_unitario', models.FloatField()),
                ('precio_unitario', models.FloatField()),
                ('costo_unitario', models.FloatField()),
                ('precio_descontado', models.FloatField()),
                ('total', models.FloatField()),
                ('descuento_total', models.FloatField()),
                ('precio_descontado_total', models.FloatField()),
                ('costo_total', models.FloatField()),
                ('utilidad', models.FloatField()),
                ('categoria', models.ForeignKey(to='moneycash.Categoria')),
                ('factura', models.ForeignKey(to='moneycash.Factura')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('existencias', models.FloatField()),
                ('descuento', models.FloatField()),
                ('precio', models.FloatField()),
                ('costo', models.FloatField()),
                ('categoria', models.ForeignKey(to='moneycash.Categoria')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('cerrado', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('numero_inicial', models.DateField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='marca',
            field=models.ForeignKey(to='moneycash.Marca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='item',
            field=models.ForeignKey(to='moneycash.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='marca',
            field=models.ForeignKey(to='moneycash.Marca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='periodo',
            field=models.ForeignKey(to='moneycash.Periodo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='serie',
            field=models.ForeignKey(to='moneycash.Serie'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caja',
            name='series',
            field=models.ManyToManyField(to='moneycash.Serie'),
            preserve_default=True,
        ),
    ]
