# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedor',
            name='plazo',
            field=models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias'),
        ),
        migrations.AlterField(
            model_name='provedor',
            name='saldo',
            field=models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True),
        ),
    ]
