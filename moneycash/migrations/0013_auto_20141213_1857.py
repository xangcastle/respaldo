# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0012_auto_20141213_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='entregada',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura',
            name='autorizada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='factura',
            name='contabilizada',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='factura',
            name='impresa',
            field=models.BooleanField(default=False),
        ),
    ]
