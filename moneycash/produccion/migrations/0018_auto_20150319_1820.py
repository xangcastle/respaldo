# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0017_auto_20150319_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='contacto',
            field=models.CharField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre_area',
            field=models.CharField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
    ]
