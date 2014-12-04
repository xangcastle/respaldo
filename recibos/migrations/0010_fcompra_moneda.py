# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0009_auto_20141203_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcompra',
            name='moneda',
            field=models.ForeignKey(to='recibos.Moneda', null=True),
            preserve_default=True,
        ),
    ]
