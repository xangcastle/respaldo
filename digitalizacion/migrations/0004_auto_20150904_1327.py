# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0003_indexacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexacion',
            options={'verbose_name_plural': 'carga de imagenes masiva'},
        ),
        migrations.AlterModelOptions(
            name='pod',
            options={'managed': False, 'verbose_name': 'comprobante', 'verbose_name_plural': 'carga de imagenes manual'},
        ),
    ]
