# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0011_auto_20141203_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='depreciacion_activo',
            field=models.FloatField(default=0.0, verbose_name=b'costos de depreciasion de activos', blank=True),
        ),
    ]
