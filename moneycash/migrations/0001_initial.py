# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='total_periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iva_pagado', models.FloatField(default=0)),
                ('iva_contra', models.FloatField(default=0)),
                ('ir_cobrado', models.FloatField(default=0)),
                ('ir_pagado', models.FloatField(default=0)),
                ('al_recaudado', models.FloatField(default=0)),
                ('al_pagado', models.FloatField(default=0)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, to='moneycash.Categoria', null=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('saldo', models.FloatField(default=0, help_text=b'saldo actual de la cuenta')),
                ('cuenta', models.ForeignKey(related_name='cuenta_madre', blank=True, to='moneycash.Cuenta', null=True)),
            ],
            options={
                'ordering': ['code'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cuenta_periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saldo_inicial', models.FloatField(default=0)),
                ('saldo_final', models.FloatField(default=0)),
                ('cuenta', models.ForeignKey(to='moneycash.Cuenta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('fecha', models.DateTimeField()),
                ('fecha_vence', models.DateField(help_text=b'si se deja en blanco se aplica el plazo del provedor', null=True, verbose_name=b'fecha de vencimiento', blank=True)),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('forma_pago', models.CharField(default=b'CO', max_length=2, verbose_name=b'forma de pago', choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO')])),
                ('subtotal', models.FloatField(default=0.0)),
                ('descuento', models.FloatField(default=0.0)),
                ('iva', models.FloatField(default=0.0)),
                ('exento_iva', models.BooleanField(default=False)),
                ('x_iva', models.FloatField(default=100, blank=True)),
                ('ir', models.FloatField(default=0.0, verbose_name=b'retencion del ir')),
                ('exento_ir', models.BooleanField(default=False)),
                ('x_ir', models.FloatField(default=100, blank=True)),
                ('al', models.FloatField(default=0.0, verbose_name=b'retencion de la alcaldia')),
                ('exento_al', models.BooleanField(default=False, verbose_name=b'exento alcaldia')),
                ('x_al', models.FloatField(default=100, blank=True)),
                ('total', models.FloatField(default=0.0)),
                ('abonado', models.FloatField(default=0.0)),
                ('saldo', models.FloatField(default=0.0)),
                ('tc', models.FloatField(default=1.0, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('existencias', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('costo', models.FloatField(default=0)),
                ('comprar', models.BooleanField(default=True)),
                ('vender', models.BooleanField(default=True)),
                ('almacenar', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(blank=True, to='moneycash.Categoria', null=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(default=1)),
                ('existencias', models.FloatField(default=0)),
                ('saldo', models.FloatField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('costo_entrada', models.FloatField(default=0)),
                ('costo_promedio', models.FloatField(default=0)),
                ('costo_importacion', models.FloatField(default=0)),
                ('costo_internacion', models.FloatField(default=0)),
                ('recibido', models.FloatField(null=True, blank=True)),
                ('documento', models.ForeignKey(blank=True, to='moneycash.Documento', null=True)),
                ('item', models.ForeignKey(to='moneycash.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debe', models.FloatField(default=0)),
                ('haber', models.FloatField(default=0)),
                ('cuenta', models.ForeignKey(to='moneycash.Cuenta')),
                ('documento', models.ForeignKey(to='moneycash.Documento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Numeracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_inicial', models.PositiveIntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('inicio_produccion', models.DateField(null=True, blank=True)),
                ('fin_produccion', models.DateField(null=True, blank=True)),
                ('inicio_ventas', models.DateField(null=True, blank=True)),
                ('fin_ventas', models.DateField(null=True, blank=True)),
                ('cerrado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-fecha_final'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='relacion_comercial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_relacion', models.CharField(default=b'CL', max_length=2, verbose_name=b'tipo de relacion', choices=[(b'CL', b'CLIENTE'), (b'PR', b'PROVEEDOR')])),
                ('tiempo_entrega', models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', null=True, verbose_name=b'tiempo de entrega')),
                ('limite_credito', models.FloatField(default=0, null=True, verbose_name=b'limite de credito', blank=True)),
                ('saldo', models.FloatField(default=0, verbose_name=b'saldo inicial', blank=True)),
                ('plazo', models.PositiveIntegerField(default=0, help_text=b'plazo de credito expresado en cantidad de dias', null=True)),
            ],
            options={
                'verbose_name': 'relacion comercial',
                'verbose_name_plural': 'relaciones comerciales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocioComercial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'socios comerciales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'sucursales',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDoc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('contabiliza', models.BooleanField(default=True, help_text=b'indica si el documento tiene afectacion contable')),
                ('afectacion', models.IntegerField(help_text=b'tipo de afectacion inventarial', choices=[(1, b'POSITIVA'), (-1, b'NEGATIVA'), (0, b'SIN AFECTACION')])),
            ],
            options={
                'verbose_name': 'tipo de documento',
                'verbose_name_plural': 'tipos de documentos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='relacion_comercial',
            name='socio',
            field=models.ForeignKey(to='moneycash.SocioComercial'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numeracion',
            name='sucursal',
            field=models.ForeignKey(to='moneycash.Sucursal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='numeracion',
            name='tipodoc',
            field=models.ForeignKey(to='moneycash.TipoDoc'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='numeracion',
            unique_together=set([('tipodoc', 'sucursal')]),
        ),
        migrations.AddField(
            model_name='item',
            name='marca',
            field=models.ForeignKey(blank=True, to='moneycash.Marca', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='bodega',
            field=models.ForeignKey(related_name='moneycash_documento_bodega', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='cliente',
            field=models.ForeignKey(related_name='moneycash_documento_cliente', blank=True, to='moneycash.SocioComercial', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='moneda',
            field=models.ForeignKey(related_name='moneycash_documento_moneda', blank=True, to='moneycash.Moneda', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='periodo',
            field=models.ForeignKey(related_name='moneycash_documento_periodo', blank=True, to='moneycash.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='proveedor',
            field=models.ForeignKey(related_name='moneycash_documento_proveedor', blank=True, to='moneycash.SocioComercial', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='sucursal',
            field=models.ForeignKey(related_name='moneycash_documento_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='tipodoc',
            field=models.ForeignKey(related_name='moneycash_documento_tipodoc', blank=True, to='moneycash.TipoDoc', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='user',
            field=models.ForeignKey(related_name='moneycash_documento_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuenta_periodo',
            name='periodo',
            field=models.ForeignKey(to='moneycash.Periodo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bodega',
            name='sucursal',
            field=models.ForeignKey(to='moneycash.Sucursal'),
            preserve_default=True,
        ),
    ]
