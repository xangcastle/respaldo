# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0002_auto_20150429_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='pod',
            field=models.FileField(null=True, upload_to=metropolitana.models.generar_ruta_comprobante, blank=True),
            preserve_default=True,
        ),
    ]
