# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_auto_20141213_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sucursal',
            options={'verbose_name_plural': 'sucursales'},
        ),
        migrations.AlterField(
            model_name='serie',
            name='numero_inicial',
            field=models.PositiveIntegerField(),
        ),
    ]
