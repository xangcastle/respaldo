# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0008_cuenta_banco_tasa_cambio'),
        ('contabilidad', '0002_auto_20150120_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta_Banco',
            fields=[
            ],
            options={
                'verbose_name': 'cuenta de banco',
                'proxy': True,
                'verbose_name_plural': 'cuentas de bancos',
            },
            bases=('moneycash.cuenta_banco',),
        ),
        migrations.CreateModel(
            name='tasa_cambio',
            fields=[
            ],
            options={
                'verbose_name': 'tasa de cambio',
                'proxy': True,
                'verbose_name_plural': 'tasas de cambio',
            },
            bases=('moneycash.tasa_cambio',),
        ),
    ]
