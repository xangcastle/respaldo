# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('encargado', models.CharField(default=b'', max_length=100)),
                ('unidad_ejecutora', models.CharField(default=b'', max_length=10)),
            ],
            options={
                'ordering': ['name'],
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
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('modelo', models.CharField(default=b'', max_length=30)),
                ('serie', models.CharField(default=b'', max_length=30)),
                ('velocidad', models.PositiveIntegerField(default=25, verbose_name=b'velocidad del equipo')),
                ('contador_inicial', models.PositiveIntegerField(default=25, help_text=b'contador que tenia el equipo al momento de la compra')),
                ('contador_actual', models.PositiveIntegerField(default=25)),
                ('vida_util', models.PositiveIntegerField(default=1000000)),
                ('precio_copia', models.FloatField(null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='equipo_periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contador_inicial', models.PositiveIntegerField()),
                ('contador_final', models.PositiveIntegerField()),
                ('equipo', models.ForeignKey(to='produccion.Equipo')),
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
                'ordering': ['name'],
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
                ('copias', models.FloatField(default=0.0)),
                ('importe', models.FloatField(default=0.0)),
                ('tc', models.FloatField(default=0.0)),
                ('area', models.ForeignKey(to='produccion.Area')),
                ('periodo', models.ForeignKey(related_name='produccion_recibo_periodo', blank=True, to='moneycash.Periodo', null=True)),
                ('sucursal', models.ForeignKey(related_name='produccion_recibo_sucursal', blank=True, to='moneycash.Sucursal', null=True)),
                ('user', models.ForeignKey(related_name='produccion_recibo_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-numero'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='recibo_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('copias', models.FloatField(default=0.0)),
                ('precio', models.FloatField(default=0.0)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
                ('equipo', models.ForeignKey(to='produccion.Equipo')),
                ('recibo', models.ForeignKey(to='produccion.Recibo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('direccion', models.TextField(max_length=250, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='equipo',
            name='marca',
            field=models.ForeignKey(to='produccion.Marca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='cliente',
            field=models.ForeignKey(to='produccion.Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='ubicacion',
            field=models.ForeignKey(to='produccion.Ubicacion'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('moneycash.periodo',),
        ),
        migrations.AddField(
            model_name='equipo_periodo',
            name='periodo',
            field=models.ForeignKey(to='produccion.Periodo'),
            preserve_default=True,
        ),
    ]
