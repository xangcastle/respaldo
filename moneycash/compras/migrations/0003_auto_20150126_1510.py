# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_categoria_marca'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comprascategoria',
            options={'verbose_name': 'categoria', 'verbose_name_plural': 'compras por categorias'},
        ),
    ]
