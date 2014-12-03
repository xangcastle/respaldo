# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0007_refaccion_oem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refaccion',
            options={'verbose_name_plural': 'refacciones'},
        ),
        migrations.AddField(
            model_name='servicio',
            name='periodo',
            field=models.ForeignKey(blank=True, to='recibos.Periodo', null=True),
            preserve_default=True,
        ),
    ]
