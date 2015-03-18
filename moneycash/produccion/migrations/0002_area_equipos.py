# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='equipos',
            field=models.ManyToManyField(to='produccion.Equipo'),
            preserve_default=True,
        ),
    ]
