# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import quickdocs.models


class Migration(migrations.Migration):

    dependencies = [
        ('quickdocs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='indice_superior',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('quickdocs.indice',),
        ),
        migrations.AlterModelOptions(
            name='indice',
            options={'ordering': ('indice',)},
        ),
        migrations.AddField(
            model_name='documento',
            name='documento',
            field=models.FileField(null=True, upload_to=quickdocs.models.get_media_url, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='indice',
            name='indice_superior',
            field=models.ForeignKey(related_name='relacion_indice_superior', blank=True, to='quickdocs.indice_superior', null=True),
            preserve_default=True,
        ),
    ]
