# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0009_compra_moneda'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='al',
            field=models.FloatField(default=0.0, verbose_name=b'retencion de la alcaldia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='ir',
            field=models.FloatField(default=0.0, verbose_name=b'retencion del ir'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='iva',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
