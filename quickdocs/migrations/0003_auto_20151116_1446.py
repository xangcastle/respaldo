# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickdocs', '0002_auto_20151110_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='indice_inferior',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('quickdocs.indice',),
        ),
        migrations.CreateModel(
            name='indice_intermedio',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('quickdocs.indice',),
        ),
        migrations.AlterField(
            model_name='indice',
            name='indice_superior',
            field=models.ForeignKey(related_name='relacion_indice_superior', blank=True, to='quickdocs.Indice', null=True),
            preserve_default=True,
        ),
    ]
