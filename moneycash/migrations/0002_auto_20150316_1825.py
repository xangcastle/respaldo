# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='fin_produccion',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='periodo',
            name='inicio_produccion',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
