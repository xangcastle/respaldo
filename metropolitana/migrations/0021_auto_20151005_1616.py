# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0020_auto_20151005_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='name_alt',
            field=models.CharField(help_text=b'se usa para evitar la duplicidad', max_length=75, null=True, verbose_name=b'nombre alternativo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name_alt',
            field=models.CharField(help_text=b'se usa para evitar la duplicidad', max_length=75, null=True, verbose_name=b'nombre alternativo', blank=True),
            preserve_default=True,
        ),
    ]
