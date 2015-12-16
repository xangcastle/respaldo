# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0022_paquete_exportado'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='indexacion',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
