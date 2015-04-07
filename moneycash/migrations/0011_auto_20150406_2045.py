# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0010_auto_20150406_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('tipo_relacion', models.CharField(default=b'CL', max_length=2, choices=[(b'CL', b'CLIENTE'), (b'PR', b'PROVEEDOR')])),
                ('tiempo_entrega', models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', null=True, verbose_name=b'tiempo de entrega')),
                ('limite_credito', models.FloatField(default=0, null=True, verbose_name=b'limite de credito', blank=True)),
                ('saldo', models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True)),
                ('plazo', models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True)),
            ],
            options={
                'db_table': 'prueba_cliente',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('tipo_relacion', models.CharField(default=b'CL', max_length=2, choices=[(b'CL', b'CLIENTE'), (b'PR', b'PROVEEDOR')])),
                ('tiempo_entrega', models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', null=True, verbose_name=b'tiempo de entrega')),
                ('limite_credito', models.FloatField(default=0, null=True, verbose_name=b'limite de credito', blank=True)),
                ('saldo', models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True)),
                ('plazo', models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True)),
            ],
            options={
                'db_table': 'prueba_cliente',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='sociocomercial',
            options={},
        ),
        migrations.AddField(
            model_name='documento',
            name='cliente',
            field=models.ForeignKey(related_name='moneycash_documento_cliente', blank=True, to='moneycash.SocioComercial', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='fecha_vence',
            field=models.DateField(help_text=b'si se deja en blanco se aplica el plazo del provedor', null=True, verbose_name=b'fecha de vencimiento', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='forma_pago',
            field=models.CharField(default=b'CO', max_length=2, verbose_name=b'forma de pago', choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='proveedor',
            field=models.ForeignKey(related_name='moneycash_documento_proveedor', blank=True, to='moneycash.SocioComercial', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='tipodoc',
            field=models.ForeignKey(related_name='moneycash_documento_tipodoc', blank=True, to='moneycash.TipoDoc', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='numeracion',
            unique_together=set([('tipodoc', 'sucursal')]),
        ),
    ]
