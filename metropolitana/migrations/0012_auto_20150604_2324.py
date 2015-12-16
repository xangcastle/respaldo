# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0011_auto_20150604_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='cerrado',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='paquete',
            name='lotificado',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
