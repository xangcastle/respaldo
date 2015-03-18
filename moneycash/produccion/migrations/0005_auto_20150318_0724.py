# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0004_auto_20150317_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='costo_compra',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipo',
            name='costo_copia',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipo',
            name='depreciacion_copia',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipo',
            name='precio_venta',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipo',
            name='valor_depreciado',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo_periodo',
            name='copias',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
