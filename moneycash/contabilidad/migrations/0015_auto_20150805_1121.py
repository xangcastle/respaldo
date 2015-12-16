# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0014_auto_20150515_0120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comprobante',
            options={'verbose_name': 'comprobantes de diario'},
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'ordering': ['code'], 'verbose_name_plural': 'catalogo de cuentas'},
        ),
    ]
