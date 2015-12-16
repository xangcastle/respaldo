# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0026_auto_20151026_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='imagen',
            field=models.FileField(null=True, upload_to=metropolitana.models.get_media_url, blank=True),
            preserve_default=True,
        ),
    ]
