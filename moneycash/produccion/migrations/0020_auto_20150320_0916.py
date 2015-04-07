# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0019_auto_20150319_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='tc',
            field=models.FloatField(default=0.0, null=True),
            preserve_default=True,
        ),
    ]
