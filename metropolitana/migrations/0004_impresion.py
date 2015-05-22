# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metropolitana', '0003_paquete_pod'),
    ]

    operations = [
        migrations.CreateModel(
            name='impresion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_verificacion', models.DateTimeField(auto_now=True)),
                ('consecutivo', models.PositiveIntegerField()),
                ('paquete', models.ForeignKey(to='metropolitana.Paquete')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
