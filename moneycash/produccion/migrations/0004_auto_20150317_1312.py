# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_auto_20150316_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipo_periodo',
            options={'verbose_name': 'equipo', 'verbose_name_plural': 'equipos en produccion'},
        ),
        migrations.AddField(
            model_name='equipo_periodo',
            name='copias',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
