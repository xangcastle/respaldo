# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articulo',
            options={'verbose_name': 'articulo', 'verbose_name_plural': 'inventario'},
        ),
        migrations.AddField(
            model_name='requisa',
            name='site',
            field=models.ForeignKey(blank=True, to='recibos.Site', null=True),
            preserve_default=True,
        ),
    ]
