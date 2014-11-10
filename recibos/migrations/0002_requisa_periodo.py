# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisa',
            name='periodo',
            field=models.ForeignKey(blank=True, to='recibos.Periodo', null=True),
            preserve_default=True,
        ),
    ]
