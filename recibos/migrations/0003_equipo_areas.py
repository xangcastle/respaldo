# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0002_requisa_periodo'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='areas',
            field=models.ManyToManyField(related_name='equipo_areas_manytomany', null=True, verbose_name='areas atendidas', to='recibos.Area', blank=True),
            preserve_default=True,
        ),
    ]
