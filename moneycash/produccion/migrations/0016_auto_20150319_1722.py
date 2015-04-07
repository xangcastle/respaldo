# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0015_auto_20150319_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thabiente',
            options={'verbose_name': 'tarjeta habiente', 'verbose_name_plural': 'tarjeta habientes'},
        ),
        migrations.AddField(
            model_name='abono',
            name='fecha',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
