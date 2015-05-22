# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0013_comprobante_diferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='comprobante_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=35, blank=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('parcial', models.FloatField(null=True, blank=True)),
                ('debe', models.FloatField(null=True, blank=True)),
                ('haber', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'contabilidad_comprobante_detalle',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.FloatField(default=0, verbose_name=b'saldo inicial'),
            preserve_default=True,
        ),
    ]
