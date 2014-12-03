# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0004_requisa_equipo'),
    ]

    operations = [
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
            name='Refaccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20, null=True, blank=True)),
                ('descripcion', models.CharField(max_length=20, null=True, blank=True)),
                ('costo', models.FloatField(null=True, blank=True)),
                ('duracion', models.IntegerField(null=True, blank=True)),
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
            ],
            options={
            },
            bases=(models.Model,),
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
    ]
