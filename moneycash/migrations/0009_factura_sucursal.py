# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0008_remove_factura_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='sucursal',
            field=models.ForeignKey(default=1, to='moneycash.Sucursal'),
            preserve_default=False,
        ),
    ]
