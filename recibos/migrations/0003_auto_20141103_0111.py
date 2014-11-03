# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0002_auto_20141103_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisa',
            name='site',
        ),
        migrations.AddField(
            model_name='requisa',
            name='site_destino',
            field=models.ForeignKey(related_name='site_destino', blank=True, to='recibos.Site', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requisa',
            name='site_origen',
            field=models.ForeignKey(related_name='site_origen', blank=True, to='recibos.Site', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='requisa',
            name='tipo_requisa',
            field=models.CharField(max_length=2, choices=[('EN', 'REQUISA DE ENTRADA'), ('SA', 'REQUISA DE SALIDA'), ('CO', 'REQUISA DE CONSUMO'), ('TR', 'REQUISA DE TRASLADO')]),
        ),
    ]
