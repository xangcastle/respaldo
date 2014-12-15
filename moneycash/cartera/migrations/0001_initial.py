# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0022_auto_20141215_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.cuenta',),
        ),
    ]
