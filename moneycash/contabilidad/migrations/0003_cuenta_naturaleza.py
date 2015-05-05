# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_periodo_cerrado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='naturaleza',
            field=models.CharField(default='AC', max_length=2, choices=[(b'AC', b'ACREDEDORA'), (b'DE', b'DEUDORA'), (b'RE', b'RESULTADOS')]),
            preserve_default=False,
        ),
    ]
