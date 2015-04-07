# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0007_auto_20150406_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, to='moneycash.Categoria', null=True)),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='categoria',
            field=models.ForeignKey(blank=True, to='moneycash.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='costo',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='descuento',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='existencias',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='precio',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='marca',
            field=models.ForeignKey(blank=True, to='moneycash.Marca', null=True),
            preserve_default=True,
        ),
    ]
