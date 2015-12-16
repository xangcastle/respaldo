# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multifilefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0009_auto_20151020_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='tar',
            name='archivos',
            field=multifilefield.models.MultiFileField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='indexacion',
            name='archivos',
            field=multifilefield.models.MultiFileField(upload_to=b''),
            preserve_default=True,
        ),
    ]
