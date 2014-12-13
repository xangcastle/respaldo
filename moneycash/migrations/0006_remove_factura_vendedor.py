# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0005_auto_20141213_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='vendedor',
        ),
    ]
