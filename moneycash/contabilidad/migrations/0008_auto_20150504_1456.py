# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0007_auto_20150430_0027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='balanza',
            options={'ordering': ['cuenta'], 'verbose_name': 'cuenta', 'verbose_name_plural': 'balanza de comprobacion'},
        ),
        migrations.AddField(
            model_name='periodo',
            name='code',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='naturaleza',
            field=models.CharField(blank=True, max_length=2, choices=[(b'AC', b'ACREDEDORA'), (b'DE', b'DEUDORA')]),
            preserve_default=True,
        ),
    ]
