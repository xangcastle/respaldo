# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0012_auto_20141227_0031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallecompra',
            options={'verbose_name': 'producto'},
        ),
        migrations.AlterField(
            model_name='compra',
            name='exento_al',
            field=models.BooleanField(default=False, verbose_name=b'exento alcaldia'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='x_al',
            field=models.FloatField(default=100, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='x_ir',
            field=models.FloatField(default=100, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='x_iva',
            field=models.FloatField(default=100, blank=True),
        ),
    ]
