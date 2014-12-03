# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0008_auto_20141203_1704'),
    ]

    operations = [
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
            name='Provedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, null=True, blank=True)),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='nombre o razon social', blank=True)),
                ('direccion', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fcompra',
            name='provedor',
            field=models.ForeignKey(to='recibos.Provedor'),
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
            model_name='contacto',
            name='provedor',
            field=models.ForeignKey(blank=True, to='recibos.Provedor', null=True),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='refaccion',
            options={'verbose_name_plural': 'refacciones y consumibles'},
        ),
        migrations.AddField(
            model_name='refaccion',
            name='minimo',
            field=models.FloatField(null=True, verbose_name='existencia minima requerida', blank=True),
            preserve_default=True,
        ),
    ]
