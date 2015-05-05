# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0002_auto_20150408_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('existencias', models.FloatField(null=True, blank=True)),
                ('ubicacion', models.CharField(max_length=10, blank=True)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='kardex',
            name='costo_anterior',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
