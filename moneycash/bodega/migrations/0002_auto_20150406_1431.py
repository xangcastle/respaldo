# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('fecha', models.DateTimeField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('subtotal', models.FloatField(default=0.0)),
                ('descuento', models.FloatField(default=0.0)),
                ('iva', models.FloatField(default=0.0)),
                ('exento_iva', models.BooleanField(default=False)),
                ('x_iva', models.FloatField(default=100, blank=True)),
                ('ir', models.FloatField(default=0.0, verbose_name=b'retencion del ir')),
                ('exento_ir', models.BooleanField(default=False)),
                ('x_ir', models.FloatField(default=100, blank=True)),
                ('al', models.FloatField(default=0.0, verbose_name=b'retencion de la alcaldia')),
                ('exento_al', models.BooleanField(default=False, verbose_name=b'exento alcaldia')),
                ('x_al', models.FloatField(default=100, blank=True)),
                ('total', models.FloatField(default=0.0)),
                ('abonado', models.FloatField(default=0.0)),
                ('saldo', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'moneycash_documento',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='kardex',
            name='documento',
        ),
    ]
