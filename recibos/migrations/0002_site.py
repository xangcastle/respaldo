# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recibos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='nombre del site', blank=True)),
                ('areas', models.ManyToManyField(to='recibos.Marca', null=True, blank=True)),
                ('encargado', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('equipos', models.ManyToManyField(to='recibos.Equipo', null=True, blank=True)),
                ('ubicacion', models.ForeignKey(blank=True, to='recibos.Ubicacion', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
