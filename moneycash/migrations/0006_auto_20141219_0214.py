# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0005_auto_20141218_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='poliza_producto',
            fields=[
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='costo',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='existencias',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
