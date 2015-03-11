# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_auto_20150310_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedor',
            name='plazo',
            field=models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True),
            preserve_default=True,
        ),
    ]
