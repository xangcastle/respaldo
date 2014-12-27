# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0011_auto_20141226_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodo',
            options={'ordering': ['-fecha_final']},
        ),
        migrations.AddField(
            model_name='compra',
            name='exento_al',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='exento_ir',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='exento_iva',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='subtotal',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='x_al',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='x_ir',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='x_iva',
            field=models.FloatField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='periodo',
            name='cerrado',
            field=models.BooleanField(default=False),
        ),
    ]
