# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0012_auto_20150505_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='diferencia',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
