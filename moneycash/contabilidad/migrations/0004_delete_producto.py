# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_auto_20141219_0214'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
