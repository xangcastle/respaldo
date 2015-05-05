# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
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
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('contrato', models.PositiveIntegerField(null=True, blank=True)),
                ('direccion', models.TextField(max_length=250, null=True, blank=True)),
                ('distribuidor', models.CharField(max_length=150, null=True, blank=True)),
                ('segmento', models.CharField(max_length=50, null=True, blank=True)),
                ('tarifa', models.CharField(max_length=70, null=True, blank=True)),
                ('servicio', models.CharField(max_length=70, null=True, blank=True)),
                ('telefono_contacto', models.CharField(max_length=70, null=True, blank=True)),
                ('valor_pagar', models.FloatField(null=True, blank=True)),
                ('barrio', models.ForeignKey(blank=True, to='metropolitana.Barrio', null=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Colector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('pendientes', models.PositiveIntegerField(null=True)),
                ('asignados', models.PositiveIntegerField(null=True)),
                ('entregados', models.PositiveIntegerField(null=True)),
                ('foto', models.FileField(null=True, upload_to=metropolitana.models.get_media_url, blank=True)),
            ],
            options={
                'verbose_name_plural': 'colectores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('pendientes', models.PositiveIntegerField(null=True)),
                ('asignados', models.PositiveIntegerField(null=True)),
                ('entregados', models.PositiveIntegerField(null=True)),
                ('codigo_telefonico', models.CharField(max_length=5, null=True, blank=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True, null=True)),
                ('numero', models.PositiveIntegerField()),
                ('avance', models.CharField(default=b'0.00 %', max_length=10, null=True, verbose_name=b'porcentaje de avance', blank=True)),
                ('cantidad_paquetes', models.PositiveIntegerField(default=0, null=True, verbose_name=b'cantidad de facturas', blank=True)),
                ('entregados', models.PositiveIntegerField(default=0, null=True, verbose_name=b'entregadas', blank=True)),
                ('cerrado', models.BooleanField(default=False)),
                ('asignado', models.BooleanField(default=False)),
                ('barrio', models.ForeignKey(blank=True, to='metropolitana.Barrio', null=True)),
                ('colector', models.ForeignKey(blank=True, to='metropolitana.Colector', null=True)),
                ('departamento', models.ForeignKey(blank=True, to='metropolitana.Departamento', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('pendientes', models.PositiveIntegerField(null=True)),
                ('asignados', models.PositiveIntegerField(null=True)),
                ('entregados', models.PositiveIntegerField(null=True)),
                ('departamento', models.ForeignKey(blank=True, to='metropolitana.Departamento', null=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.CharField(max_length=100, null=True, blank=True)),
                ('consecutivo', models.PositiveIntegerField(null=True, blank=True)),
                ('contrato', models.PositiveIntegerField(null=True, blank=True)),
                ('factura', models.CharField(max_length=70, null=True, blank=True)),
                ('ciclo', models.PositiveIntegerField(null=True, blank=True)),
                ('mes', models.PositiveIntegerField(null=True, blank=True)),
                ('ano', models.PositiveIntegerField(null=True, blank=True)),
                ('cliente', models.CharField(max_length=150, null=True, blank=True)),
                ('direccion', models.TextField(max_length=250, null=True, blank=True)),
                ('barrio', models.CharField(max_length=150, null=True, blank=True)),
                ('municipio', models.CharField(max_length=150, null=True, blank=True)),
                ('departamento', models.CharField(max_length=150, null=True, blank=True)),
                ('distribuidor', models.CharField(max_length=150, null=True, blank=True)),
                ('ruta', models.CharField(max_length=25, null=True, blank=True)),
                ('zona', models.PositiveIntegerField(null=True, blank=True)),
                ('telefono', models.CharField(max_length=50, null=True, blank=True)),
                ('segmento', models.CharField(max_length=50, null=True, blank=True)),
                ('tarifa', models.CharField(max_length=70, null=True, blank=True)),
                ('idbarrio', models.PositiveIntegerField(null=True, blank=True)),
                ('iddepartemento', models.PositiveIntegerField(null=True, blank=True)),
                ('idmunicipio', models.PositiveIntegerField(null=True, blank=True)),
                ('servicio', models.CharField(max_length=70, null=True, blank=True)),
                ('cupon', models.PositiveIntegerField(null=True, blank=True)),
                ('total_mes_factura', models.FloatField(null=True, blank=True)),
                ('valor_pagar', models.FloatField(null=True, blank=True)),
                ('entrega', models.BooleanField(default=False, verbose_name=b'entregada')),
                ('numero_fiscal', models.PositiveIntegerField(null=True, blank=True)),
                ('factura_interna', models.PositiveIntegerField(null=True, blank=True)),
                ('telefono_contacto', models.CharField(max_length=70, null=True, blank=True)),
                ('estado', models.CharField(default=b'PE', max_length=2, choices=[(b'PE', b'PENDIENTE'), (b'EN', b'ENTREGADO'), (b'AS', b'ASIGNADO')])),
                ('lotificado', models.BooleanField(default=False)),
                ('cerrado', models.BooleanField(default=False)),
                ('comprobante', models.FileField(null=True, upload_to=metropolitana.models.get_media_url, blank=True)),
                ('barra', models.CharField(max_length=30, null=True, blank=True)),
                ('colector', models.ForeignKey(blank=True, to='metropolitana.Colector', null=True)),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='metropolitana.Lote', null=True)),
            ],
            options={
                'ordering': ['consecutivo'],
                'verbose_name': 'factura',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lote',
            name='municipio',
            field=models.ForeignKey(blank=True, to='metropolitana.Municipio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='departamento',
            field=models.ForeignKey(blank=True, to='metropolitana.Departamento', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='municipio',
            field=models.ForeignKey(blank=True, to='metropolitana.Municipio', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barrio',
            name='departamento',
            field=models.ForeignKey(blank=True, to='metropolitana.Departamento', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='barrio',
            name='municipio',
            field=models.ForeignKey(blank=True, to='metropolitana.Municipio', null=True),
            preserve_default=True,
        ),
    ]
