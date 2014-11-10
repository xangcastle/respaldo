# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.equipo',),
        ),
        migrations.CreateModel(
            name='marca',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.marca',),
        ),
    ]
