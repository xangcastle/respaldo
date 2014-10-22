# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0004_auto_20141021_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(to='recibos.Marca', null=True),
        ),
    ]
