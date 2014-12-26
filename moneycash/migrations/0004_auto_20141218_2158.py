# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneycash', '0003_auto_20141216_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=False)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('periodo', models.ForeignKey(related_name=b'moneycash_compra_periodo', blank=True, to='moneycash.Periodo', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('costo_promedio', models.FloatField(default=0)),
                ('costo_importacion', models.FloatField(default=0)),
                ('costo_internacion', models.FloatField(default=0)),
                ('recibido', models.FloatField(null=True, blank=True)),
                ('compra', models.ForeignKey(blank=True, to='moneycash.Compra', null=True)),
                ('item', models.ForeignKey(to='moneycash.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetallePoliza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factura', models.ForeignKey(to='moneycash.Compra')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=False)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('periodo', models.ForeignKey(related_name=b'moneycash_poliza_periodo', blank=True, to='moneycash.Periodo', null=True)),
                ('sucursal', models.ForeignKey(related_name=b'moneycash_poliza_sucursal', blank=True, to='moneycash.Sucursal', null=True)),
                ('user', models.ForeignKey(related_name=b'moneycash_poliza_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('tipo', models.CharField(default=b'LO', max_length=2, choices=[(b'LO', b'NACIONAL'), (b'EX', b'EXTRAJERO')])),
                ('tiempo_entrega', models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia, 0 equivale a entrega inmediata', verbose_name=b'tiempo de entrega')),
                ('limite_credito', models.FloatField(null=True, blank=True)),
                ('saldo', models.FloatField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoCosto',
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
            model_name='detallepoliza',
            name='poliza',
            field=models.ForeignKey(to='moneycash.Poliza'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='provedor',
            field=models.ForeignKey(to='moneycash.Provedor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='sucursal',
            field=models.ForeignKey(related_name=b'moneycash_compra_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_costo',
            field=models.ForeignKey(to='moneycash.TipoCosto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='user',
            field=models.ForeignKey(related_name=b'moneycash_compra_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
