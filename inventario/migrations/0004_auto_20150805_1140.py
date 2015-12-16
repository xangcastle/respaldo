# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20150805_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['rack', 'columna', 'fila', 'codigo']},
        ),
        migrations.AddField(
            model_name='producto',
            name='con_diferencia',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
