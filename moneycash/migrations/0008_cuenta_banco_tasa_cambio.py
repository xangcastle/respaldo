# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0007_tipo_movimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta_Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('balance_inicial', models.FloatField()),
                ('balance_actual', models.FloatField()),
                ('es_tarjeta', models.BooleanField(default=False)),
                ('banco', models.ForeignKey(to='moneycash.Banco')),
                ('moneda', models.ForeignKey(to='moneycash.Moneda')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tasa_cambio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('tipo_cambio', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
