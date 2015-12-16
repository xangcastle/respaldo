# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0007_auto_20150925_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=b'TEMP')),
            ],
            options={
                'verbose_name': 'archivo tar',
                'verbose_name_plural': 'carga de archivos tar',
            },
            bases=(models.Model,),
        ),
    ]
