# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0010_auto_20141226_1253'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='compra',
            unique_together=set([('provedor', 'numero')]),
        ),
    ]
