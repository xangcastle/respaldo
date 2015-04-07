# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0013_auto_20150319_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='tc',
            field=models.FloatField(default=1.0),
            preserve_default=True,
        ),
    ]
