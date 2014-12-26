# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20141226_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalle',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'detalle de productos'},
        ),
    ]
