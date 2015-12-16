# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0017_auto_20151125_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexacion',
            options={'verbose_name': 'archivos pdf', 'verbose_name_plural': 'carga de imagenes masiva'},
        ),
    ]
