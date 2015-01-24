# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='duracion_toner',
            field=models.PositiveIntegerField(help_text=b'duracion del toner copias', null=True, blank=True),
            preserve_default=True,
        ),
    ]
