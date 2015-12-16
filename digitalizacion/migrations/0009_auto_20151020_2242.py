# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multifilefield.models
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0008_tar'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexacion',
            name='carpeta',
            field=models.CharField(max_length=8, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='indexacion',
            name='resumen',
            field=models.TextField(max_length=65, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='indexacion',
            name='archivos',
            field=multifilefield.models.MultiFileField(upload_to=metropolitana.models.get_media_url),
            preserve_default=True,
        ),
    ]
