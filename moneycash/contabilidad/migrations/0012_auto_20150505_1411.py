# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0011_migracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='concepto',
            field=models.TextField(max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='migracion',
            name='concepto',
            field=models.TextField(max_length=400),
            preserve_default=True,
        ),
    ]
