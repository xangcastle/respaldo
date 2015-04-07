# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0005_auto_20150330_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipodoc',
            old_name='afectation',
            new_name='afectacion',
        ),
    ]
