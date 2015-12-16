# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0004_auto_20150904_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idempleado', models.PositiveIntegerField(null=True, verbose_name=b'codigo de empleado', blank=True)),
                ('nombre', models.CharField(max_length=120, null=True, blank=True)),
                ('cedula', models.CharField(max_length=14, null=True, blank=True)),
                ('gerencia', models.CharField(max_length=65, null=True, blank=True)),
                ('localidad', models.CharField(max_length=65, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
