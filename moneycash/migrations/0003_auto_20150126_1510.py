# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_auto_20150125_2307'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterModelOptions(
            name='bodega',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='caja',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'ordering': ['name']},
        ),
    ]
