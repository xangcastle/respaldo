# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0010_auto_20150604_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='import_paquete',
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
                ('idbarrio', models.IntegerField(null=True, blank=True)),
                ('iddepartamento', models.IntegerField(null=True, blank=True)),
                ('idmunicipio', models.IntegerField(null=True, blank=True)),
                ('servicio', models.CharField(max_length=70, null=True, blank=True)),
                ('cupon', models.PositiveIntegerField(null=True, blank=True)),
                ('total_mes_factura', models.FloatField(null=True, blank=True)),
                ('valor_pagar', models.FloatField(null=True, blank=True)),
                ('numero_fiscal', models.PositiveIntegerField(null=True, blank=True)),
                ('factura_interna', models.PositiveIntegerField(null=True, blank=True)),
                ('telefono_contacto', models.CharField(max_length=70, null=True, blank=True)),
            ],
            options={
                'db_table': 'metropolitana_paquete',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='paquete',
            name='entrega',
            field=models.NullBooleanField(default=False, verbose_name=b'entregada'),
            preserve_default=True,
        ),
    ]
