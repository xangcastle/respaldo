# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0018_auto_20141213_2353'),
        ('facturacion', '0002_proforma'),
        ('caja', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='impresas',
        ),
        migrations.CreateModel(
            name='abonos_factura',
            fields=[
            ],
            options={
                'verbose_name': 'factura',
                'proxy': True,
                'verbose_name_plural': 'detalle de facturas canceladas',
            },
            bases=('moneycash.detalle_pago',),
        ),
        migrations.CreateModel(
            name='CierreCaja',
            fields=[
            ],
            options={
                'verbose_name': 'cierre de caja',
                'proxy': True,
                'verbose_name_plural': 'cierres de caja',
            },
            bases=('moneycash.cierrecaja',),
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.deposito',),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
            ],
            options={
                'verbose_name': 'factura',
                'proxy': True,
                'verbose_name_plural': 'facturas impresas',
            },
            bases=('facturacion.factura',),
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
        migrations.CreateModel(
            name='Recibo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.recibo',),
        ),
    ]
