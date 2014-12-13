# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0007_factura_vendedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='sucursal',
        ),
    ]
