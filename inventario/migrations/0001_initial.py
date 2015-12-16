# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=250)),
                ('marca', models.CharField(max_length=30)),
                ('rack', models.CharField(max_length=4)),
                ('columna', models.CharField(max_length=2)),
                ('fila', models.CharField(max_length=2)),
                ('costo', models.FloatField()),
                ('existencia', models.FloatField()),
                ('conteo1', models.FloatField()),
                ('conteo2', models.FloatField()),
                ('conteo3', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
