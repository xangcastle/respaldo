# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multifilefield.models
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0010_auto_20151020_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tar',
            options={'verbose_name': 'archivos', 'verbose_name_plural': 'carga de archivos'},
        ),
        migrations.AddField(
            model_name='tar',
            name='aplicar_ocr',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tar',
            name='archivos',
            field=multifilefield.models.MultiFileField(null=True, upload_to=metropolitana.models.get_media_url, blank=True),
            preserve_default=True,
        ),
    ]
