# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import digitalizacion.models
import multifilefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0012_auto_20151020_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexacion',
            name='carpeta',
            field=models.CharField(max_length=8, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='indexacion',
            name='archivos',
            field=multifilefield.models.MultiFileField(upload_to=digitalizacion.models.get_path),
            preserve_default=True,
        ),
    ]
