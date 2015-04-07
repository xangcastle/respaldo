# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0011_factura_detalle_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura_detalle',
            name='item',
            field=models.ForeignKey(blank=True, to='produccion.Area', null=True),
            preserve_default=True,
        ),
    ]
