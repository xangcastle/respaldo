# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0009_auto_20150406_1502'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relacion_comercial',
            old_name='tipo',
            new_name='tipo_relacion',
        ),
        migrations.RemoveField(
            model_name='relacion_comercial',
            name='cs1',
        ),
        migrations.RemoveField(
            model_name='relacion_comercial',
            name='cs2',
        ),
        migrations.AddField(
            model_name='relacion_comercial',
            name='socio',
            field=models.ForeignKey(default=1, to='moneycash.SocioComercial'),
            preserve_default=False,
        ),
    ]
