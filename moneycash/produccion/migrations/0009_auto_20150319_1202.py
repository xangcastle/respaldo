# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_auto_20150316_1825'),
        ('produccion', '0008_auto_20150319_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='retener_al',
            new_name='exento_ir',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='retener_ir',
        ),
        migrations.AddField(
            model_name='cliente',
            name='limite_credito',
            field=models.FloatField(default=0, null=True, verbose_name=b'limite de credito', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='plazo',
            field=models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='saldo',
            field=models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='abonado',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='comentarios',
            field=models.TextField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='exento_al',
            field=models.BooleanField(default=False, verbose_name=b'exento alcaldia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='moneda',
            field=models.ForeignKey(related_name='produccion_factura_moneda', default=1, to='moneycash.Moneda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='x_al',
            field=models.FloatField(default=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='x_ir',
            field=models.FloatField(default=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='x_iva',
            field=models.FloatField(default=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura',
            name='al',
            field=models.FloatField(default=0.0, verbose_name=b'retencion de la alcaldia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_vence',
            field=models.DateField(help_text=b'si se deja en blanco se aplica el plazo del provedor', null=True, verbose_name=b'fecha de vencimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura',
            name='ir',
            field=models.FloatField(default=0.0, verbose_name=b'retencion del ir'),
            preserve_default=True,
        ),
    ]
