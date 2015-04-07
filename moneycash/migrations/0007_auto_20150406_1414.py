# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0006_auto_20150330_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='total_periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iva_pagado', models.FloatField(default=0)),
                ('iva_contra', models.FloatField(default=0)),
                ('ir_cobrado', models.FloatField(default=0)),
                ('ir_pagado', models.FloatField(default=0)),
                ('al_recaudado', models.FloatField(default=0)),
                ('al_pagado', models.FloatField(default=0)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('sucursal', models.ForeignKey(to='moneycash.Sucursal')),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='documento',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tipodoc',
            options={'verbose_name': 'tipo de documento', 'verbose_name_plural': 'tipos de documentos'},
        ),
        migrations.AddField(
            model_name='documento',
            name='bodega',
            field=models.ForeignKey(related_name='moneycash_documento_bodega', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipodoc',
            name='afectacion',
            field=models.IntegerField(help_text=b'tipo de afectacion inventarial', choices=[(1, b'POSITIVA'), (-1, b'NEGATIVA'), (0, b'SIN AFECTACION')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tipodoc',
            name='contabiliza',
            field=models.BooleanField(default=True, help_text=b'indica si el documento tiene afectacion contable'),
            preserve_default=True,
        ),
    ]
