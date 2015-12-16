# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0016_auto_20150716_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipificacion',
            options={'verbose_name_plural': 'tipificaciones'},
        ),
        migrations.AlterField(
            model_name='paquete',
            name='tipificacion',
            field=models.ForeignKey(default=1, blank=True, to='metropolitana.Tipificacion', null=True),
            preserve_default=True,
        ),
    ]
