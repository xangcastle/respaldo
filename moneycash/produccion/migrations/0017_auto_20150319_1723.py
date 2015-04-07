# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0016_auto_20150319_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abono',
            name='th',
        ),
        migrations.DeleteModel(
            name='abono',
        ),
        migrations.DeleteModel(
            name='thabiente',
        ),
    ]
