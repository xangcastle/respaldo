# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0003_provedor_plazo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='contado',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='credito',
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo',
            field=models.CharField(default=b'CR', max_length=2, verbose_name=b'tipo de pago de la compra'),
            preserve_default=True,
        ),
    ]
