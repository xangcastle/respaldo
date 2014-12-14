# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0010_auto_20141213_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='bodegas',
            field=models.ManyToManyField(to=b'moneycash.Bodega', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
