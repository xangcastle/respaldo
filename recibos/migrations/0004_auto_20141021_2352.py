# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0003_auto_20141021_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='areas',
            field=models.ManyToManyField(to=b'recibos.Area', null=True, blank=True),
        ),
    ]
