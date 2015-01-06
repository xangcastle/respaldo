# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0004_auto_20150105_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_vence',
            field=models.DateField(help_text=b'si se deja en blanco se aplica el plazo del provedor', null=True, verbose_name=b'fecha de vencimiento', blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='tipo',
            field=models.CharField(default=b'CR', max_length=2, verbose_name=b'tipo de pago de la compra', choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')]),
        ),
    ]
