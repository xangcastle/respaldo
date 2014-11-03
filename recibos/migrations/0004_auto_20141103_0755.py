# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0003_auto_20141103_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisa',
            name='site_destino',
        ),
        migrations.RemoveField(
            model_name='requisa',
            name='site_origen',
        ),
        migrations.AddField(
            model_name='requisa',
            name='site',
            field=models.ForeignKey(blank=True, to='recibos.Site', null=True),
            preserve_default=True,
        ),
    ]
