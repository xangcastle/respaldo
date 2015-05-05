# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0009_auto_20150504_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='code',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='sucursal',
            field=models.CharField(max_length=65, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='naturaleza',
            field=models.CharField(blank=True, max_length=2, choices=[(b'AC', b'ACREDEDORA'), (b'DE', b'DEUDORA')]),
            preserve_default=True,
        ),
    ]
