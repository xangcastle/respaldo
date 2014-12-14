# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneycash', '0017_auto_20141213_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('monto', models.FloatField()),
                ('banco', models.ForeignKey(to='moneycash.Banco')),
                ('caja', models.ForeignKey(related_name=b'moneycash_deposito_caja', blank=True, to='moneycash.Caja', null=True)),
                ('cierre_caja', models.ForeignKey(related_name=b'moneycash_deposito_cierre_caja', blank=True, to='moneycash.CierreCaja', null=True)),
                ('periodo', models.ForeignKey(related_name=b'moneycash_deposito_periodo', blank=True, to='moneycash.Periodo', null=True)),
                ('sucursal', models.ForeignKey(related_name=b'moneycash_deposito_sucursal', blank=True, to='moneycash.Sucursal', null=True)),
                ('user', models.ForeignKey(related_name=b'moneycash_deposito_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='abonos_factura',
        ),
        migrations.DeleteModel(
            name='pago_cheque',
        ),
        migrations.DeleteModel(
            name='pago_credito',
        ),
        migrations.DeleteModel(
            name='pago_efectivo',
        ),
        migrations.DeleteModel(
            name='pago_tarjeta',
        ),
        migrations.DeleteModel(
            name='pago_transferencia',
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='saldo_final',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='saldo_inicial',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pago',
            name='capitalizable',
            field=models.BooleanField(default=True, help_text=b'indica si este tipo de pago aplica en el cierre de caja'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cierrecaja',
            name='sucursal',
            field=models.ForeignKey(related_name=b'moneycash_cierrecaja_sucursal', blank=True, to='moneycash.Sucursal', null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='sucursal',
            field=models.ForeignKey(related_name=b'moneycash_factura_sucursal', blank=True, to='moneycash.Sucursal', null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='sucursal',
            field=models.ForeignKey(related_name=b'moneycash_recibo_sucursal', blank=True, to='moneycash.Sucursal', null=True),
        ),
    ]
