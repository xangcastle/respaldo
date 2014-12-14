# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneycash', '0015_auto_20141213_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='CierreCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('apertura', models.DateTimeField(null=True, blank=True)),
                ('cierre', models.DateTimeField(null=True, blank=True)),
                ('cerrado', models.BooleanField(default=False)),
                ('caja', models.ForeignKey(to='moneycash.Caja')),
                ('periodo', models.ForeignKey(related_name=b'moneycash_cierrecaja_periodo', blank=True, to='moneycash.Periodo', null=True)),
                ('user', models.ForeignKey(related_name=b'moneycash_cierrecaja_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
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
        migrations.RemoveField(
            model_name='factura',
            name='vendedor',
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='saldo',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='total',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='cierre_caja',
            field=models.ForeignKey(related_name=b'moneycash_factura_cierre_caja', blank=True, to='moneycash.CierreCaja', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='user',
            field=models.ForeignKey(related_name=b'moneycash_factura_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibo',
            name='cierre_caja',
            field=models.ForeignKey(related_name=b'moneycash_recibo_cierre_caja', blank=True, to='moneycash.CierreCaja', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibo',
            name='user',
            field=models.ForeignKey(related_name=b'moneycash_recibo_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='factura',
            name='periodo',
            field=models.ForeignKey(related_name=b'moneycash_factura_periodo', blank=True, to='moneycash.Periodo', null=True),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='periodo',
            field=models.ForeignKey(related_name=b'moneycash_recibo_periodo', blank=True, to='moneycash.Periodo', null=True),
        ),
    ]
