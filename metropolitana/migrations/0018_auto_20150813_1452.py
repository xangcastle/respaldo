# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0017_auto_20150805_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impresion',
            name='paquete',
        ),
        migrations.RemoveField(
            model_name='impresion',
            name='user',
        ),
        migrations.DeleteModel(
            name='impresion',
        ),
        migrations.AlterModelOptions(
            name='estadisticaciclo',
            options={'managed': False, 'verbose_name': 'estadistica'},
        ),
        migrations.RemoveField(
            model_name='colector',
            name='asignados',
        ),
        migrations.RemoveField(
            model_name='colector',
            name='entregados',
        ),
        migrations.RemoveField(
            model_name='colector',
            name='pendientes',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='asignados',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='entregados',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='pendientes',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='asignados',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='entregados',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='pendientes',
        ),
        migrations.AlterField(
            model_name='paquete',
            name='tipificacion',
            field=models.ForeignKey(blank=True, to='metropolitana.Tipificacion', null=True),
            preserve_default=True,
        ),
    ]
