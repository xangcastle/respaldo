# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='contado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='credito',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='fecha_vence',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
