# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0008_auto_20150406_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='relacion_comercial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(default=b'CL', max_length=2, choices=[(b'CL', b'CLIENTE'), (b'PR', b'PROVEEDOR')])),
                ('tiempo_entrega', models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', null=True, verbose_name=b'tiempo de entrega')),
                ('limite_credito', models.FloatField(default=0, null=True, verbose_name=b'limite de credito', blank=True)),
                ('saldo', models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True)),
                ('plazo', models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocioComercial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='relacion_comercial',
            name='cs1',
            field=models.ForeignKey(related_name='sc1', to='moneycash.SocioComercial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relacion_comercial',
            name='cs2',
            field=models.ForeignKey(related_name='sc2', to='moneycash.SocioComercial'),
            preserve_default=True,
        ),
    ]
