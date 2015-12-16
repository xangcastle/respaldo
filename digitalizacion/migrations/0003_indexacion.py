# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multifilefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0002_auto_20150813_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indexacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('archivos', multifilefield.models.MultiFileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
