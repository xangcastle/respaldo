# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0004_auto_20141103_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisa',
            old_name='site',
            new_name='site_origen',
        ),
    ]
