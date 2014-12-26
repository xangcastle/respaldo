# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0007_auto_20141225_1611'),
    ]

    operations = [
        migrations.DeleteModel(
            name='poliza_producto',
        ),
        migrations.AlterModelOptions(
            name='provedor',
            options={'verbose_name_plural': 'provedores'},
        ),
        migrations.AlterField(
            model_name='banco',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='provedor',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='serie',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
        migrations.AlterField(
            model_name='tipocosto',
            name='code',
            field=models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True),
        ),
    ]
