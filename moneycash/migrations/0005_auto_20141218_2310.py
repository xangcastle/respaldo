# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0004_auto_20141218_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='tipo_costo',
        ),
        migrations.AddField(
            model_name='detallepoliza',
            name='tipo_costo',
            field=models.ForeignKey(default=1, to='moneycash.TipoCosto'),
            preserve_default=False,
        ),
    ]
