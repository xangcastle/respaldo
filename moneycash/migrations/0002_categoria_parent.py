# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='parent',
            field=models.ForeignKey(blank=True, to='moneycash.Categoria', null=True),
            preserve_default=True,
        ),
    ]
