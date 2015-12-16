# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0015_auto_20150714_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('causa', models.CharField(max_length=35, verbose_name=b'causa unificada')),
                ('descripcion', models.TextField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='paquete',
            name='tipificacion',
            field=models.ForeignKey(blank=True, to='metropolitana.Tipificacion', null=True),
            preserve_default=True,
        ),
    ]
