# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_auto_20150316_1825'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produccion', '0006_equipo_ubicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
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
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.PositiveIntegerField(null=True, blank=True)),
                ('autorizado', models.BooleanField(default=True)),
                ('impreso', models.BooleanField(default=False)),
                ('contabilizado', models.BooleanField(default=False)),
                ('entregado', models.BooleanField(default=False)),
                ('exento_iva', models.BooleanField(default=False)),
                ('retener_al', models.BooleanField(default=False)),
                ('retener_ir', models.BooleanField(default=False)),
                ('subtotal', models.FloatField(default=0.0)),
                ('descuento', models.FloatField(default=0.0)),
                ('iva', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('ir', models.FloatField(default=0.0)),
                ('al', models.FloatField(default=0.0)),
                ('cliente', models.ForeignKey(to='produccion.Cliente')),
                ('periodo', models.ForeignKey(related_name='produccion_factura_periodo', blank=True, to='moneycash.Periodo', null=True)),
                ('sucursal', models.ForeignKey(related_name='produccion_factura_sucursal', blank=True, to='moneycash.Sucursal', null=True)),
                ('user', models.ForeignKey(related_name='produccion_factura_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-numero'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='factura_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField()),
                ('precio', models.FloatField()),
                ('factura', models.ForeignKey(to='produccion.Factura')),
            ],
            options={
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
                ('precio', models.FloatField(default=0.0)),
                ('categoria', models.ForeignKey(to='produccion.Categoria')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='item',
            field=models.ForeignKey(to='produccion.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='costo_compra',
            field=models.FloatField(null=True, verbose_name=b'costo de compra', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='depreciacion_copia',
            field=models.FloatField(null=True, verbose_name=b'depreciacion por copia', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='precio_venta',
            field=models.FloatField(null=True, verbose_name=b'valor en libros', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='valor_depreciado',
            field=models.FloatField(null=True, verbose_name=b'total depreciado', blank=True),
            preserve_default=True,
        ),
    ]
