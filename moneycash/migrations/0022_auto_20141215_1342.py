# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0021_auto_20141215_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('cargo', models.CharField(max_length=100, null=True, verbose_name=b'cargo que ocupa', blank=True)),
                ('telefono', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('cliente', models.ForeignKey(to='moneycash.Cliente')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cliente',
            name='identificacion',
            field=models.CharField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuenta',
            name='numero_cuenta',
            field=models.CharField(default=' ', max_length=25),
            preserve_default=False,
        ),
    ]
