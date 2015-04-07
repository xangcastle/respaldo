# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0004_auto_20150326_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
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
        migrations.AddField(
            model_name='item',
            name='marca',
            field=models.ForeignKey(default=1, to='moneycash.Marca'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='saldo',
            field=models.FloatField(default=0, help_text=b'saldo actual de la cuenta'),
            preserve_default=True,
        ),
    ]
