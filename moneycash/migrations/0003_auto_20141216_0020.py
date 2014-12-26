# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_categoria_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categoria',
            field=models.ForeignKey(blank=True, to='moneycash.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='marca',
            field=models.ForeignKey(blank=True, to='moneycash.Marca', null=True),
        ),
    ]
