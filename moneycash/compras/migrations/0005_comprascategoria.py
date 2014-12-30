# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasCategoria',
            fields=[
            ],
            options={
                'db_table': 'compras_categoria',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
