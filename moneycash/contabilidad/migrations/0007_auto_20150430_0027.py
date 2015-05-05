# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0006_auto_20150430_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='sumas_iguales',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='total_debe',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='total_haber',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='fecha',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
