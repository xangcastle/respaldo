# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0008_auto_20150504_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operativa',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('contabilidad.cuenta',),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='saldo_actual',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='naturaleza',
            field=models.CharField(default=b'DE', max_length=2, blank=True, choices=[(b'AC', b'ACREDEDORA'), (b'DE', b'DEUDORA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.FloatField(default=0, help_text=b'saldo inicial de la cuenta', verbose_name=b'saldo inicial'),
            preserve_default=True,
        ),
    ]
