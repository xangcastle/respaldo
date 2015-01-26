# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0003_auto_20150125_2213'),
        ('moneycash', '0011_auto_20150125_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
    ]
