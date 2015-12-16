# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0018_auto_20150813_1452'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('digitalizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impresion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_verificacion', models.DateTimeField(auto_now=True, verbose_name=b'fecha de carga')),
                ('consecutivo', models.PositiveIntegerField()),
                ('archivo', models.CharField(max_length=100, null=True, blank=True)),
                ('paquete', models.ForeignKey(to='metropolitana.Paquete')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['consecutivo'],
                'db_table': 'metropolitana_impresion',
                'verbose_name_plural': 'impresion de comprobantes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='import_paquete',
            options={'managed': False, 'verbose_name': 'factura', 'verbose_name_plural': 'importacion de facturas'},
        ),
    ]
