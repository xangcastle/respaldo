# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0004_tc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tc',
            options={'verbose_name': 'tasa de cambio', 'verbose_name_plural': 'tasas de cambio'},
        ),
    ]
