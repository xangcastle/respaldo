# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name='Area')),
                ('responsable', models.CharField(max_length=50, verbose_name='Responsable de Area')),
                ('codigo', models.IntegerField(verbose_name='Unidad Ejecutora')),
            ],
            options={
                'ordering': ('nombre', 'responsable'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=30, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=300)),
                ('costo', models.FloatField()),
                ('caracteristicas', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('area', models.ForeignKey(to='recibos.Area')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Detalles por Area',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DetalleRequisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField()),
                ('costo', models.FloatField()),
                ('articulo', models.ForeignKey(to='recibos.Articulo')),
            ],
            options={
                'verbose_name': 'articulo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=50)),
                ('serie', models.CharField(max_length=50)),
                ('contador', models.IntegerField(default=0)),
                ('minimo', models.IntegerField(default=0)),
                ('velocidad', models.IntegerField(verbose_name='Copias x Minuto')),
                ('papel', models.BooleanField(default=False, verbose_name='Incluye Papel')),
                ('operador', models.BooleanField(default=False, verbose_name='Incluye Operador')),
                ('precio_copia', models.FloatField(verbose_name='Precio x Copias')),
                ('comentarios', models.CharField(max_length=400, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('costo', models.FloatField(null=True, blank=True)),
                ('vida_util', models.PositiveIntegerField(help_text='vida util en cantidad de copias', null=True, blank=True)),
            ],
            options={
                'ordering': ('modelo',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name='Marca')),
                ('tipo', models.CharField(max_length=2, choices=[('OR', 'FABRICANTE ORIGINAL'), ('GE', 'REMPLAZO GENERICO')])),
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
                ('cerrado', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-fecha_inicial',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contador_inicial', models.IntegerField()),
                ('contador_final', models.IntegerField(null=True)),
                ('precio_copia', models.FloatField(verbose_name='precio por copia')),
                ('meta', models.FloatField(null=True, verbose_name='meta proyectada', blank=True)),
                ('costo_partes', models.FloatField(default=0.0, help_text='suma de los costos de consumibles y partes usadas', null=True, verbose_name='costos de partes', blank=True)),
                ('costo_papel', models.FloatField(default=0.0, null=True, verbose_name='costos de papel', blank=True)),
                ('tasa_cambio', models.FloatField(null=True, verbose_name='tasa de cambio', blank=True)),
                ('equipo', models.ForeignKey(to='recibos.Equipo')),
                ('periodo', models.ForeignKey(to='recibos.Periodo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_requisa', models.CharField(max_length=2, choices=[('EN', 'ENTRADA'), ('SA', 'SALIDA')])),
                ('fecha', models.DateField()),
                ('recibido', models.CharField(max_length=300, null=True, blank=True)),
                ('entregado', models.CharField(max_length=300, null=True, blank=True)),
                ('area', models.ForeignKey(blank=True, to='recibos.Area', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=400)),
            ],
            options={
                'verbose_name_plural': 'Ubicaciones',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='equipo',
            name='marca',
            field=models.ForeignKey(to='recibos.Marca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='equipo',
            name='ubicacion',
            field=models.ForeignKey(verbose_name='Ubicacion del Equipo', blank=True, to='recibos.Ubicacion', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallerequisa',
            name='requisa',
            field=models.ForeignKey(to='recibos.Requisa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle',
            name='recibo',
            field=models.ForeignKey(to='recibos.Recibo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(to='recibos.Marca', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='equipo',
            field=models.ForeignKey(verbose_name='Impresora por Defecto', blank=True, to='recibos.Equipo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='ubicacion',
            field=models.ForeignKey(to='recibos.Ubicacion'),
            preserve_default=True,
        ),
    ]