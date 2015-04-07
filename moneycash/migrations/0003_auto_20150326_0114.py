# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moneycash', '0002_auto_20150316_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuenta_periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saldo_inicial', models.FloatField(default=0)),
                ('saldo_final', models.FloatField(default=0)),
                ('cuenta', models.ForeignKey(to='moneycash.Cuenta')),
                ('periodo', models.ForeignKey(to='moneycash.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='datos_factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('moneda', models.ForeignKey(related_name='moneycash_documento_moneda', blank=True, to='moneycash.Moneda', null=True)),
                ('periodo', models.ForeignKey(related_name='moneycash_documento_periodo', blank=True, to='moneycash.Periodo', null=True)),
                ('sucursal', models.ForeignKey(related_name='moneycash_documento_sucursal', blank=True, to='moneycash.Sucursal', null=True)),
            ],
            options={
                'ordering': ['-numero'],
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
            ],
            options={
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
                ('sucursal', models.ForeignKey(to='moneycash.Sucursal')),
            ],
            options={
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
                ('contabiliza', models.BooleanField(default=True)),
                ('afectation', models.IntegerField(choices=[(1, b'POSITIVA'), (-1, b'NEGATIVA'), (0, b'SIN AFECTACION')])),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='tipo_movimiento',
            new_name='Item',
        ),
        migrations.RemoveField(
            model_name='bodega',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='series',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='caja',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='cierrecaja',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='bodegas',
        ),
        migrations.DeleteModel(
            name='Bodega',
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.RemoveField(
            model_name='cuenta_banco',
            name='banco',
        ),
        migrations.RemoveField(
            model_name='cuenta_banco',
            name='moneda',
        ),
        migrations.DeleteModel(
            name='Cuenta_Banco',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='banco',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='caja',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='cierre_caja',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='deposito',
            name='user',
        ),
        migrations.DeleteModel(
            name='Deposito',
        ),
        migrations.RemoveField(
            model_name='detalle_pago',
            name='banco',
        ),
        migrations.DeleteModel(
            name='Banco',
        ),
        migrations.RemoveField(
            model_name='detalle_pago',
            name='cuenta',
        ),
        migrations.RemoveField(
            model_name='detalle_pago',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='detalle_pago',
            name='pago',
        ),
        migrations.RemoveField(
            model_name='detalle_pago',
            name='recibo',
        ),
        migrations.DeleteModel(
            name='detalle_pago',
        ),
        migrations.RemoveField(
            model_name='detallepoliza',
            name='poliza',
        ),
        migrations.RemoveField(
            model_name='detallepoliza',
            name='tipo_costo',
        ),
        migrations.DeleteModel(
            name='DetallePoliza',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='user',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='Pago',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='poliza',
            name='user',
        ),
        migrations.DeleteModel(
            name='Poliza',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='caja',
        ),
        migrations.DeleteModel(
            name='Caja',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='cierre_caja',
        ),
        migrations.DeleteModel(
            name='CierreCaja',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='periodo',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='sucursal',
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='user',
        ),
        migrations.DeleteModel(
            name='Recibo',
        ),
        migrations.DeleteModel(
            name='Serie',
        ),
        migrations.DeleteModel(
            name='tasa_cambio',
        ),
        migrations.DeleteModel(
            name='TipoCosto',
        ),
        migrations.AddField(
            model_name='numeracion',
            name='tipodoc',
            field=models.ForeignKey(to='moneycash.TipoDoc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kardex',
            name='item',
            field=models.ForeignKey(to='moneycash.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='tipodoc',
            field=models.ForeignKey(related_name='moneycash_documento_documento', blank=True, to='moneycash.TipoDoc', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='documento',
            name='user',
            field=models.ForeignKey(related_name='moneycash_documento_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'ordering': ['code']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['code']},
        ),
        migrations.AlterModelOptions(
            name='moneda',
            options={'ordering': ['code']},
        ),
        migrations.AlterModelOptions(
            name='sucursal',
            options={'ordering': ['code']},
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='limite_credito',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='numero_cuenta',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='plazo',
        ),
        migrations.AddField(
            model_name='periodo',
            name='fin_ventas',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='periodo',
            name='inicio_ventas',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
