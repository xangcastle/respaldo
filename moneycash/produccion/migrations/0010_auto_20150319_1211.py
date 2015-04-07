# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0009_auto_20150319_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='item',
        ),
        migrations.AddField(
            model_name='area',
            name='item',
            field=models.ForeignKey(verbose_name=b'plan de facturarion', blank=True, to='produccion.Item', null=True),
            preserve_default=True,
        ),
    ]
