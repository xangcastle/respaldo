# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0019_auto_20150925_0734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zona_barrio',
            options={'verbose_name': 'barrio', 'verbose_name_plural': 'barrios incluidos'},
        ),
        migrations.AddField(
            model_name='departamento',
            name='name_alt',
            field=models.CharField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
    ]
