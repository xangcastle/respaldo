# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multifilefield.models
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0011_auto_20151020_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexacion',
            name='carpeta',
        ),
        migrations.AlterField(
            model_name='indexacion',
            name='archivos',
            field=multifilefield.models.MultiFileField(upload_to=metropolitana.models.get_media_url),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tar',
            name='archivos',
            field=multifilefield.models.MultiFileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
