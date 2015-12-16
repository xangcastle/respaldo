# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.FloatField()),
                ('existencia', models.FloatField()),
                ('imagen', models.FileField(upload_to=b'tienda')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
