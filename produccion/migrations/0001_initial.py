# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='produccion_equipo',
            fields=[
            ],
            options={
                'verbose_name': 'equipo',
                'proxy': True,
                'verbose_name_plural': 'equipos en produccion',
            },
            bases=('recibos.recibo',),
        ),
    ]
