# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0010_auto_20150319_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura_detalle',
            name='total',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
