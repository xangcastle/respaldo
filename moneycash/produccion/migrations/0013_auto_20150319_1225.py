# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0012_auto_20150319_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura_detalle',
            name='area',
            field=models.ForeignKey(blank=True, to='produccion.Area', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='item',
            field=models.ForeignKey(default=1, to='produccion.Item'),
            preserve_default=False,
        ),
    ]
