# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0005_auto_20141103_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisa',
            name='site_destino',
            field=models.ForeignKey(related_name='requisa_site_destino', blank=True, to='recibos.Site', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisa',
            name='site_origen',
            field=models.ForeignKey(related_name='requisa_site_origen', blank=True, to='recibos.Site', null=True),
        ),
    ]
