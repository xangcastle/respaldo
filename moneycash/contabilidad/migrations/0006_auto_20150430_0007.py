# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0005_auto_20150429_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprobante',
            name='autorizado',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='bodega',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='contabilizado',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='entregado',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='fecha_vence',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='forma_pago',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='impreso',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='tipodoc',
        ),
        migrations.AddField(
            model_name='comprobante',
            name='concepto',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='periodo',
            field=models.ForeignKey(related_name='contabilidad_comprobante_periodo', blank=True, to='contabilidad.Periodo', null=True),
            preserve_default=True,
        ),
    ]
