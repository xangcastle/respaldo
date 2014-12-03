# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0004_requisa_equipo'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='site_equipo',
        ),
        migrations.DeleteModel(
            name='site_inventario',
        ),
        migrations.DeleteModel(
            name='site_requisa',
        ),
        migrations.DeleteModel(
            name='site_site',
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.articulo',),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.equipo',),
        ),
        migrations.CreateModel(
            name='Requisa',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.requisa',),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('recibos.site',),
        ),
    ]
