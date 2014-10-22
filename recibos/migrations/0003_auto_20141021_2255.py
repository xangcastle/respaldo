# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0002_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(to='recibos.Area', null=True),
        ),
    ]
