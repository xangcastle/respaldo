# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0006_empleado_ecuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='ecuenta',
            field=models.FileField(upload_to=metropolitana.models.get_media_url, null=True, verbose_name=b'estado de cuenta', blank=True),
            preserve_default=True,
        ),
    ]
