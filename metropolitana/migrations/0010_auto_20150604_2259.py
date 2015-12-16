# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0009_paquete_idcliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano', models.IntegerField(null=True, blank=True)),
                ('mes', models.IntegerField(null=True, blank=True)),
                ('ciclo', models.IntegerField(null=True, blank=True)),
                ('total', models.FloatField(null=True, blank=True)),
                ('entregados', models.FloatField(null=True, blank=True)),
                ('pendientes', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'metropolitana_estadistica',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='paquete',
            options={'ordering': ['cliente'], 'verbose_name': 'factura'},
        ),
        migrations.RemoveField(
            model_name='paquete',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='paquete',
            name='pod',
        ),
    ]
