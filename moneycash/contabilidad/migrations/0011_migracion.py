# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0010_auto_20150505_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='migracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('poliza', models.CharField(max_length=30, null=True, blank=True)),
                ('concepto', models.CharField(max_length=150)),
                ('sucursal', models.CharField(max_length=65, null=True, blank=True)),
                ('numero_cuenta', models.CharField(max_length=30, null=True, blank=True)),
                ('nombre_cuenta', models.CharField(max_length=65, null=True, blank=True)),
                ('debe', models.FloatField(default=0)),
                ('haber', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'comprobante',
                'verbose_name_plural': 'migracion de comprobantes',
            },
            bases=(models.Model,),
        ),
    ]
