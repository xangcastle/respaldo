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
            name='Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
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
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CierreCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('apertura', models.DateTimeField(null=True, blank=True)),
                ('saldo_inicial', models.FloatField(default=0)),
                ('cierre', models.DateTimeField(null=True, blank=True)),
                ('saldo_final', models.FloatField(default=0)),
                ('cerrado', models.BooleanField(default=False)),
                ('caja', models.ForeignKey(to='moneycash.Caja')),
            ],
            options={
                'ordering': ['-numero'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
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
                ('limite_credito', models.FloatField(default=0.0)),
                ('plazo', models.FloatField(default=0.0)),
                ('saldo', models.FloatField(default=0.0)),
                ('bodegas', models.ManyToManyField(to='moneycash.Bodega', null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('cargo', models.CharField(max_length=100, null=True, verbose_name=b'cargo que ocupa', blank=True)),
                ('telefono', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('cliente', models.ForeignKey(to='moneycash.Cliente')),
            ],
            options={
                'ordering': ['name'],
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
                ('numero_cuenta', models.CharField(max_length=25)),
                ('limite_credito', models.FloatField()),
                ('plazo', models.PositiveIntegerField()),
                ('saldo', models.FloatField(null=True, blank=True)),
                ('cliente', models.ForeignKey(to='moneycash.Cliente')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cuenta_Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('balance_inicial', models.FloatField()),
                ('balance_actual', models.FloatField()),
                ('es_tarjeta', models.BooleanField(default=False)),
                ('banco', models.ForeignKey(to='moneycash.Banco')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('monto', models.FloatField()),
                ('banco', models.ForeignKey(to='moneycash.Banco')),
                ('caja', models.ForeignKey(related_name='moneycash_deposito_caja', blank=True, to='moneycash.Caja', null=True)),
                ('cierre_caja', models.ForeignKey(related_name='moneycash_deposito_cierre_caja', blank=True, to='moneycash.CierreCaja', null=True)),
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
                ('total', models.FloatField(default=0)),
                ('saldo', models.FloatField(default=0)),
                ('numero_cheque', models.CharField(max_length=25, null=True, blank=True)),
                ('numero_transferencia', models.CharField(max_length=25, null=True, blank=True)),
                ('banco', models.ForeignKey(blank=True, to='moneycash.Banco', null=True)),
                ('cuenta', models.ForeignKey(blank=True, to='moneycash.Cuenta', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetallePoliza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Empresa',
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
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('cliente_codigo', models.CharField(max_length=30, null=True, blank=True)),
                ('cliente_nombre', models.CharField(max_length=60, null=True, blank=True)),
                ('cliente_telefono', models.CharField(max_length=25, null=True, blank=True)),
                ('cliente_direccion', models.CharField(max_length=150, null=True, blank=True)),
                ('cliente_ident', models.CharField(max_length=25, null=True, blank=True)),
                ('subtotal', models.FloatField(default=0.0)),
                ('descuento', models.FloatField(default=0.0)),
                ('iva', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('saldo', models.FloatField(default=0.0)),
                ('fecha_vence', models.DateField(help_text=b'si se deja en blanco se aplica el plazo del cliente', null=True, verbose_name=b'fecha de vencimiento', blank=True)),
                ('exento_iva', models.BooleanField(default=False)),
                ('x_iva', models.FloatField(default=100, blank=True)),
                ('ir', models.FloatField(default=0.0, verbose_name=b'retencion del ir')),
                ('exento_ir', models.BooleanField(default=True)),
                ('x_ir', models.FloatField(default=100, blank=True)),
                ('al', models.FloatField(default=0.0, verbose_name=b'retencion de la alcaldia')),
                ('exento_al', models.BooleanField(default=True, verbose_name=b'exento alcaldia')),
                ('x_al', models.FloatField(default=100, blank=True)),
                ('tipo', models.CharField(default=b'CR', max_length=2, verbose_name=b'tipo de pago de la factura', choices=[(b'CO', b'CONTADO'), (b'CR', b'CREDITO'), (b'CS', b'CONSIGNACION')])),
                ('comentarios', models.TextField(max_length=400, null=True, blank=True)),
                ('cliente', models.ForeignKey(blank=True, to='moneycash.Cliente', null=True)),
            ],
            options={
                'ordering': ['-numero'],
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
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('capitalizable', models.BooleanField(default=True, help_text=b'indica si este tipo de pago aplica en el cierre de caja')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('cerrado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-fecha_final'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('periodo', models.ForeignKey(related_name='moneycash_poliza_periodo', blank=True, to='moneycash.Periodo', null=True)),
            ],
            options={
                'ordering': ['-numero'],
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
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('concepto', models.CharField(max_length=200, null=True, blank=True)),
                ('monto', models.FloatField(default=0)),
                ('caja', models.ForeignKey(related_name='moneycash_recibo_caja', blank=True, to='moneycash.Caja', null=True)),
                ('cierre_caja', models.ForeignKey(related_name='moneycash_recibo_cierre_caja', blank=True, to='moneycash.CierreCaja', null=True)),
                ('cliente', models.ForeignKey(blank=True, to='moneycash.Cliente', null=True)),
                ('periodo', models.ForeignKey(related_name='moneycash_recibo_periodo', blank=True, to='moneycash.Periodo', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('numero_inicial', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
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
            name='tasa_cambio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('tipo_cambio', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tipo_movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoCosto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recibo',
            name='sucursal',
            field=models.ForeignKey(related_name='moneycash_recibo_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibo',
            name='user',
            field=models.ForeignKey(related_name='moneycash_recibo_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='poliza',
            name='sucursal',
            field=models.ForeignKey(related_name='moneycash_poliza_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='poliza',
            name='user',
            field=models.ForeignKey(related_name='moneycash_poliza_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='moneda',
            field=models.ForeignKey(default=1, to='moneycash.Moneda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='periodo',
            field=models.ForeignKey(related_name='moneycash_factura_periodo', blank=True, to='moneycash.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='sucursal',
            field=models.ForeignKey(related_name='moneycash_factura_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='user',
            field=models.ForeignKey(related_name='moneycash_factura_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallepoliza',
            name='poliza',
            field=models.ForeignKey(to='moneycash.Poliza'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallepoliza',
            name='tipo_costo',
            field=models.ForeignKey(to='moneycash.TipoCosto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='moneda',
            field=models.ForeignKey(to='moneycash.Moneda'),
            preserve_default=True,
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
        migrations.AddField(
            model_name='deposito',
            name='moneda',
            field=models.ForeignKey(related_name='moneycash_deposito_caja', default=1, to='moneycash.Moneda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposito',
            name='periodo',
            field=models.ForeignKey(related_name='moneycash_deposito_periodo', blank=True, to='moneycash.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposito',
            name='sucursal',
            field=models.ForeignKey(related_name='moneycash_deposito_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposito',
            name='user',
            field=models.ForeignKey(related_name='moneycash_deposito_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuenta_banco',
            name='moneda',
            field=models.ForeignKey(to='moneycash.Moneda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='periodo',
            field=models.ForeignKey(related_name='moneycash_cierrecaja_periodo', blank=True, to='moneycash.Periodo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='sucursal',
            field=models.ForeignKey(related_name='moneycash_cierrecaja_sucursal', blank=True, to='moneycash.Sucursal', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='user',
            field=models.ForeignKey(related_name='moneycash_cierrecaja_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caja',
            name='series',
            field=models.ManyToManyField(to='moneycash.Serie'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caja',
            name='sucursal',
            field=models.ForeignKey(to='moneycash.Sucursal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bodega',
            name='sucursal',
            field=models.ForeignKey(to='moneycash.Sucursal'),
            preserve_default=True,
        ),
    ]
