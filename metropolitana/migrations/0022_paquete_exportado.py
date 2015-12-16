# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0021_auto_20151005_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='exportado',
            field=models.NullBooleanField(default=False, verbose_name=b'exportado'),
            preserve_default=True,
        ),
    ]
