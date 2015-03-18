# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0005_auto_20150318_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='ubicacion',
            field=models.ForeignKey(blank=True, to='produccion.Ubicacion', null=True),
            preserve_default=True,
        ),
    ]
