# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0005_auto_20150414_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='fecha',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
