# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0005_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='ecuenta',
            field=models.FileField(null=True, upload_to=metropolitana.models.get_media_url, blank=True),
            preserve_default=True,
        ),
    ]
