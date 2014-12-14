# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneycash', '0016_auto_20141213_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recibo',
            name='cajero',
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='sucursal',
            field=models.ForeignKey(related_name=b'moneycash_cierrecaja_sucursal', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='caja',
            field=models.ForeignKey(related_name=b'moneycash_factura_caja', blank=True, to='moneycash.Caja', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura',
            name='sucursal',
            field=models.ForeignKey(related_name=b'moneycash_factura_sucursal', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='caja',
            field=models.ForeignKey(related_name=b'moneycash_recibo_caja', blank=True, to='moneycash.Caja', null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='sucursal',
            field=models.ForeignKey(related_name=b'moneycash_recibo_sucursal', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
