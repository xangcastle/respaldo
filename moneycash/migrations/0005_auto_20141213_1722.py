# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0004_serie_numero_inicial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodega',
            name='sucursal',
            field=models.ForeignKey(default=1, to='moneycash.Sucursal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caja',
            name='sucursal',
            field=models.ForeignKey(default=1, to='moneycash.Sucursal'),
            preserve_default=False,
        ),
    ]
