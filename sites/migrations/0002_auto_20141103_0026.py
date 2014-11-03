# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0002_auto_20141103_0026'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='site',
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
        migrations.AlterModelOptions(
            name='site_inventario',
            options={},
        ),
        migrations.AlterModelOptions(
            name='site_requisa',
            options={},
        ),
    ]
