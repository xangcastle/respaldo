# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0005_auto_20141203_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refaccion',
            name='descripcion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
