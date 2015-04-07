# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0007_auto_20150318_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura_detalle',
            options={'verbose_name': 'item', 'verbose_name_plural': 'productos o servicios'},
        ),
        migrations.AddField(
            model_name='equipo',
            name='item',
            field=models.ForeignKey(verbose_name=b'plan de facturarion', blank=True, to='produccion.Item', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='fecha_vence',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='saldo',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='tipo',
            field=models.CharField(default=b'CR', max_length=2, verbose_name=b'tipo de pago de la compra', choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='descuento',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='cantidad',
            field=models.FloatField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura_detalle',
            name='precio',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
