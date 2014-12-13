# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0003_auto_20141213_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='numero_inicial',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
