# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0015_auto_20151026_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexacion',
            name='resumen',
            field=models.TextField(default=b'', max_length=2000, null=True),
            preserve_default=True,
        ),
    ]
