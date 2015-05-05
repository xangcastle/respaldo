# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0006_auto_20150429_2357'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contabilidad', '0004_comprobante_movimiento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comprobante',
            options={'ordering': ['-numero']},
        ),
        migrations.AddField(
            model_name='comprobante',
            name='autorizado',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='bodega',
            field=models.ForeignKey(related_name='contabilidad_comprobante_bodega', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='cliente',
            field=models.ForeignKey(related_name='contabilidad_comprobante_cliente', blank=True, to='moneycash.SocioComercial', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='contabilizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='fecha',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='fecha_vence',
            field=models.DateField(help_text=b'si se deja en blanco se aplica el plazo del provedor', null=True, verbose_name=b'fecha de vencimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='forma_pago',
            field=models.CharField(default=b'CO', max_length=2, verbose_name=b'forma de pago', choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='impreso',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='moneda',
            field=models.ForeignKey(related_name='contabilidad_comprobante_moneda', blank=True, to='moneycash.Moneda', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='numero',
            field=models.PositiveIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='periodo',
            field=models.ForeignKey(related_name='contabilidad_comprobante_periodo', blank=True, to='moneycash.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='proveedor',
            field=models.ForeignKey(related_name='contabilidad_comprobante_proveedor', blank=True, to='moneycash.SocioComercial', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='sucursal',
            field=models.ForeignKey(related_name='contabilidad_comprobante_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='tipodoc',
            field=models.ForeignKey(related_name='contabilidad_comprobante_tipodoc', blank=True, to='moneycash.TipoDoc', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='user',
            field=models.ForeignKey(related_name='contabilidad_comprobante_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
