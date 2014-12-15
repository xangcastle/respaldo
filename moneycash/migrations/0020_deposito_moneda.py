# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0019_auto_20141214_0234'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposito',
            name='moneda',
            field=models.ForeignKey(default=1, to='moneycash.Moneda'),
            preserve_default=False,
        ),
    ]
