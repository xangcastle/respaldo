# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0003_auto_20150326_0114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='datos_factura',
        ),
        migrations.AddField(
            model_name='cuenta',
            name='cuenta',
            field=models.ForeignKey(related_name='cuenta_madre', blank=True, to='moneycash.Cuenta', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='abonado',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='al',
            field=models.FloatField(default=0.0, verbose_name=b'retencion de la alcaldia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='descuento',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='exento_al',
            field=models.BooleanField(default=False, verbose_name=b'exento alcaldia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='exento_ir',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='exento_iva',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='ir',
            field=models.FloatField(default=0.0, verbose_name=b'retencion del ir'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='iva',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='saldo',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='subtotal',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='total',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='x_al',
            field=models.FloatField(default=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='x_ir',
            field=models.FloatField(default=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='x_iva',
            field=models.FloatField(default=100, blank=True),
            preserve_default=True,
        ),
    ]
