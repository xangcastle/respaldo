# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0008_auto_20141226_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='moneda',
            field=models.ForeignKey(default=1, to='moneycash.Moneda'),
            preserve_default=True,
        ),
    ]
