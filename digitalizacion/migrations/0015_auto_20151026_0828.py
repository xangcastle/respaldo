# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import digitalizacion.models
import multifilefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0014_auto_20151021_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexacion',
            name='archivos',
            field=multifilefield.models.MultiFileField(null=True, upload_to=digitalizacion.models.get_path, blank=True),
            preserve_default=True,
        ),
    ]
