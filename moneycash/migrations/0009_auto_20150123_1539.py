# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0008_cuenta_banco_tasa_cambio'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='abonado',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='saldo',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
