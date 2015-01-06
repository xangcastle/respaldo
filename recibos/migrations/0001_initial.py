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
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Area')),
                ('responsable', models.CharField(max_length=50, verbose_name=b'Responsable de Area')),
                ('codigo', models.IntegerField(verbose_name=b'Unidad Ejecutora')),
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
                'verbose_name': 'articulo',
                'verbose_name_plural': 'inventario',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cambio_partes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField(default=0)),
                ('costo', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('comprar', models.BooleanField(default=True)),
                ('vender', models.BooleanField(default=True)),
                ('almacenar', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('cargo', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=100, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
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
            name='dtCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.FloatField()),
                ('precio', models.FloatField()),
            ],
            options={
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
                ('velocidad', models.IntegerField(verbose_name=b'Copias x Minuto')),
                ('papel', models.BooleanField(default=False, verbose_name=b'Incluye Papel')),
                ('operador', models.BooleanField(default=False, verbose_name=b'Incluye Operador')),
                ('precio_copia', models.FloatField(verbose_name=b'Precio x Copias')),
                ('comentarios', models.CharField(max_length=400, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('costo', models.FloatField(null=True, blank=True)),
                ('vida_util', models.PositiveIntegerField(help_text=b'vida util en cantidad de copias', null=True, blank=True)),
                ('areas', models.ManyToManyField(related_name=b'equipo_areas_manytomany', null=True, verbose_name=b'areas atendidas', to='recibos.Area', blank=True)),
            ],
            options={
                'ordering': ('modelo',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Marca')),
                ('tipo', models.CharField(max_length=2, choices=[(b'OR', b'FABRICANTE ORIGINAL'), (b'GE', b'REMPLAZO GENERICO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('simbolo', models.CharField(max_length=3)),
                ('nombre', models.CharField(max_length=50, null=True)),
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
            name='Provedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, null=True, blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name=b'nombre o razon social', blank=True)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contador_inicial', models.IntegerField()),
                ('contador_final', models.IntegerField(null=True)),
                ('precio_copia', models.FloatField(verbose_name=b'precio por copia')),
                ('meta', models.FloatField(help_text=b'meta asignada al inicio del periodo', null=True, verbose_name=b'meta proyectada', blank=True)),
                ('costo_partes', models.FloatField(default=0.0, help_text=b'suma de los costos de consumibles y partes usadas', null=True, verbose_name=b'costos de partes', blank=True)),
                ('costo_papel', models.FloatField(default=0.0, null=True, verbose_name=b'costos de papel', blank=True)),
                ('costo_administrativo', models.FloatField(default=0.0, null=True, verbose_name=b'costos administrativos', blank=True)),
                ('depreciacion_activo', models.FloatField(default=0.0, verbose_name=b'costos de depreciasion de activos', blank=True)),
                ('tasa_cambio', models.FloatField(null=True, verbose_name=b'tasa de cambio', blank=True)),
                ('equipo', models.ForeignKey(to='recibos.Equipo')),
                ('periodo', models.ForeignKey(to='recibos.Periodo')),
            ],
            options={
                'db_table': 'view_recibos_recibo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Refaccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, null=True, blank=True)),
                ('oem', models.CharField(max_length=20, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=200, null=True, blank=True)),
                ('costo', models.FloatField(null=True, blank=True)),
                ('duracion', models.IntegerField(null=True, blank=True)),
                ('minimo', models.FloatField(null=True, verbose_name=b'existencia minima requerida', blank=True)),
                ('categoria', models.ForeignKey(to='recibos.Categoria', null=True)),
            ],
            options={
                'verbose_name_plural': 'refacciones y consumibles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Requisa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_requisa', models.CharField(max_length=2, choices=[(b'EN', b'REQUISA DE ENTRADA'), (b'SA', b'REQUISA DE SALIDA'), (b'CO', b'REQUISA DE CONSUMO')])),
                ('fecha', models.DateField()),
                ('recibido', models.CharField(max_length=300, null=True, blank=True)),
                ('entregado', models.CharField(max_length=300, null=True, blank=True)),
                ('area', models.ForeignKey(blank=True, to='recibos.Area', null=True)),
                ('equipo', models.ForeignKey(blank=True, to='recibos.Equipo', null=True)),
                ('periodo', models.ForeignKey(blank=True, to='recibos.Periodo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('numero', models.IntegerField(null=True, blank=True)),
                ('obserbaciones', models.TextField(max_length=500, null=True, blank=True)),
                ('equipo', models.ForeignKey(blank=True, to='recibos.Equipo', null=True)),
                ('periodo', models.ForeignKey(blank=True, to='recibos.Periodo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'nombre del site', blank=True)),
                ('areas', models.ManyToManyField(to='recibos.Area', null=True, blank=True)),
                ('encargado', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('equipos', models.ManyToManyField(to='recibos.Equipo', null=True, blank=True)),
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
            model_name='site',
            name='ubicacion',
            field=models.ForeignKey(blank=True, to='recibos.Ubicacion', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requisa',
            name='site_destino',
            field=models.ForeignKey(related_name=b'requisa_site_destino', blank=True, to='recibos.Site', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='requisa',
            name='site_origen',
            field=models.ForeignKey(related_name=b'requisa_site_origen', blank=True, to='recibos.Site', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fcompra',
            name='moneda',
            field=models.ForeignKey(to='recibos.Moneda', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fcompra',
            name='provedor',
            field=models.ForeignKey(to='recibos.Provedor'),
            preserve_default=True,
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
            field=models.ForeignKey(verbose_name=b'Ubicacion del Equipo', blank=True, to='recibos.Ubicacion', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dtcompra',
            name='factura',
            field=models.ForeignKey(to='recibos.FCompra'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dtcompra',
            name='item',
            field=models.ForeignKey(to='recibos.Refaccion'),
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
            model_name='contacto',
            name='provedor',
            field=models.ForeignKey(blank=True, to='recibos.Provedor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cambio_partes',
            name='refaccion',
            field=models.ForeignKey(to='recibos.Refaccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cambio_partes',
            name='servicio',
            field=models.ForeignKey(to='recibos.Servicio'),
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
            field=models.ForeignKey(verbose_name=b'Impresora por Defecto', blank=True, to='recibos.Equipo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='ubicacion',
            field=models.ForeignKey(to='recibos.Ubicacion'),
            preserve_default=True,
        ),
    ]
