# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0006_auto_20141103_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibo',
            name='costo_administrativo',
            field=models.FloatField(default=0.0, help_text='suma de los costos de consumibles y partes usadas', null=True, verbose_name='costos de partes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibo',
            name='depreciacion_activo',
            field=models.FloatField(default=0.0, null=True, verbose_name='costos de papel', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisa',
            name='tipo_requisa',
            field=models.CharField(max_length=2, choices=[('EN', 'REQUISA DE ENTRADA'), ('SA', 'REQUISA DE SALIDA'), ('CO', 'REQUISA DE CONSUMO')]),
        ),
    ]
