# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneycash', '0013_auto_20141213_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='detalle_pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.FloatField(default=0)),
                ('numero_cheque', models.CharField(max_length=25, null=True, blank=True)),
                ('numero_transferencia', models.CharField(max_length=25, null=True, blank=True)),
                ('banco', models.ForeignKey(blank=True, to='moneycash.Banco', null=True)),
                ('factura', models.ForeignKey(blank=True, to='moneycash.Factura', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('concepto', models.CharField(max_length=200, null=True, blank=True)),
                ('monto', models.FloatField(default=0)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('caja', models.ForeignKey(to='moneycash.Caja')),
                ('cajero', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cliente', models.ForeignKey(blank=True, to='moneycash.Cliente', null=True)),
                ('periodo', models.ForeignKey(to='moneycash.Periodo')),
                ('sucursal', models.ForeignKey(to='moneycash.Sucursal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='pago',
            field=models.ForeignKey(to='moneycash.Pago'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='recibo',
            field=models.ForeignKey(blank=True, to='moneycash.Recibo', null=True),
            preserve_default=True,
        ),
    ]
