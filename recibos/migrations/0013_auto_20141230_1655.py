# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0012_auto_20141225_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='meta',
            field=models.FloatField(help_text=b'meta asignada al inicio del periodo', null=True, verbose_name=b'meta proyectada', blank=True),
        ),
    ]
