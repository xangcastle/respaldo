# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0018_auto_20141213_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='comentarios',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='telefono',
        ),
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(blank=True, to='moneycash.Cliente', help_text=b'BUSCAR CLIENTE', null=True),
        ),
    ]
