# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_area_equipos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recibo_detalle',
            options={'verbose_name': 'equipo', 'verbose_name_plural': 'detalle de copias por equipo'},
        ),
        migrations.AlterField(
            model_name='area',
            name='equipos',
            field=models.ManyToManyField(to='produccion.Equipo', verbose_name=b'equipos que usa el area'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='contador_actual',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='contador_inicial',
            field=models.PositiveIntegerField(default=0, help_text=b'contador que tenia el equipo al momento de la compra'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='velocidad',
            field=models.PositiveIntegerField(default=0, verbose_name=b'velocidad del equipo'),
            preserve_default=True,
        ),
    ]
