# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedor',
            name='tiempo_entrega',
            field=models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', null=True, verbose_name=b'tiempo de entrega'),
            preserve_default=True,
        ),
    ]
