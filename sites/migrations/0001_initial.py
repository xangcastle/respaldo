# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='site_equipo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.equipo',),
        ),
        migrations.CreateModel(
            name='site_inventario',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.articulo',),
        ),
        migrations.CreateModel(
            name='site_requisa',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.requisa',),
        ),
        migrations.CreateModel(
            name='site_site',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.site',),
        ),
    ]
