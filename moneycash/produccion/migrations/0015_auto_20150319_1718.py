# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0014_factura_tc'),
    ]

    operations = [
        migrations.CreateModel(
            name='abono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='thabiente',
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
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='abono',
            name='th',
            field=models.ForeignKey(to='produccion.thabiente'),
            preserve_default=True,
        ),
    ]
