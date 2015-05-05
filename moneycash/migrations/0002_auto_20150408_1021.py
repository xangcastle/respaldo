# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('tipo_relacion', models.CharField(default=b'CL', max_length=2, verbose_name=b'tipo de relacion', choices=[(b'CL', b'CLIENTE'), (b'PR', b'PROVEEDOR')])),
                ('tiempo_entrega', models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', null=True, verbose_name=b'tiempo de entrega')),
                ('limite_credito', models.FloatField(default=0, null=True, verbose_name=b'limite de credito', blank=True)),
                ('saldo', models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True)),
                ('plazo', models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True)),
            ],
            options={
                'db_table': 'prueba_cliente',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('tipo_relacion', models.CharField(default=b'CL', max_length=2, verbose_name=b'tipo de relacion', choices=[(b'CL', b'CLIENTE'), (b'PR', b'PROVEEDOR')])),
                ('tiempo_entrega', models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', null=True, verbose_name=b'tiempo de entrega')),
                ('limite_credito', models.FloatField(default=0, null=True, verbose_name=b'limite de credito', blank=True)),
                ('saldo', models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True)),
                ('plazo', models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True)),
            ],
            options={
                'db_table': 'prueba_cliente',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='factor',
            field=models.FloatField(default=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kardex',
            name='bodega',
            field=models.ForeignKey(blank=True, to='moneycash.Bodega', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kardex',
            name='ubicacion',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
