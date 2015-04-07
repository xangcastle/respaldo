# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0018_auto_20150319_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='tc',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
