# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0014_auto_20141213_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('limite_credito', models.FloatField()),
                ('plazo', models.PositiveIntegerField()),
                ('saldo', models.FloatField(null=True, blank=True)),
                ('cliente', models.ForeignKey(to='moneycash.Cliente')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pago_cheque',
            fields=[
            ],
            options={
                'verbose_name': 'cheque',
                'proxy': True,
                'verbose_name_plural': 'pagos con cheque',
            },
            bases=('moneycash.detalle_pago',),
        ),
        migrations.CreateModel(
            name='pago_credito',
            fields=[
            ],
            options={
                'verbose_name': 'cuenta',
                'proxy': True,
                'verbose_name_plural': 'cargos a cuentas de credito',
            },
            bases=('moneycash.detalle_pago',),
        ),
        migrations.CreateModel(
            name='pago_efectivo',
            fields=[
            ],
            options={
                'verbose_name': 'monto',
                'proxy': True,
                'verbose_name_plural': 'pagos en efectivo',
            },
            bases=('moneycash.detalle_pago',),
        ),
        migrations.CreateModel(
            name='pago_tarjeta',
            fields=[
            ],
            options={
                'verbose_name': 'transaccion',
                'proxy': True,
                'verbose_name_plural': 'pagos con tarjeta de credito',
            },
            bases=('moneycash.detalle_pago',),
        ),
        migrations.CreateModel(
            name='pago_transferencia',
            fields=[
            ],
            options={
                'verbose_name': 'transaccion',
                'proxy': True,
                'verbose_name_plural': 'pagos via transferencia bancaria',
            },
            bases=('moneycash.detalle_pago',),
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='cuenta',
            field=models.ForeignKey(blank=True, to='moneycash.Cuenta', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='moneda',
            field=models.ForeignKey(default=1, to='moneycash.Moneda'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(blank=True, to='moneycash.Cliente', null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='periodo',
            field=models.ForeignKey(related_name=b'moneycash_factura_cliente', blank=True, to='moneycash.Periodo', null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='serie',
            field=models.ForeignKey(blank=True, to='moneycash.Serie', null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='sucursal',
            field=models.ForeignKey(blank=True, to='moneycash.Sucursal', null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='vendedor',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='caja',
            field=models.ForeignKey(blank=True, to='moneycash.Caja', null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='cajero',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='periodo',
            field=models.ForeignKey(related_name=b'moneycash_recibo_cliente', blank=True, to='moneycash.Periodo', null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='sucursal',
            field=models.ForeignKey(blank=True, to='moneycash.Sucursal', null=True),
        ),
    ]
