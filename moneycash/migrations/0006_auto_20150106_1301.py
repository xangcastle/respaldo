# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0005_auto_20150105_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='comentarios',
            field=models.TextField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provedor',
            name='saldo',
            field=models.FloatField(null=True, verbose_name=b'saldo inicial', blank=True),
        ),
    ]
