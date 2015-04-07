# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0011_auto_20150406_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='tc',
            field=models.FloatField(default=1.0, null=True),
            preserve_default=True,
        ),
    ]
