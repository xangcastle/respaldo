# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0003_equipo_areas'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisa',
            name='equipo',
            field=models.ForeignKey(blank=True, to='recibos.Equipo', null=True),
            preserve_default=True,
        ),
    ]