# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0012_auto_20150604_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='entrega_numero',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
