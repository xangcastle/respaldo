# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0006_auto_20150601_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='idmunicipio',
            field=models.ForeignKey(db_column=b'idmunicipio', blank=True, to='metropolitana.Municipio', null=True),
            preserve_default=True,
        ),
    ]
