# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalizacion', '0016_auto_20151116_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indexacion',
            options={'verbose_name': 'archivo pdf', 'verbose_name_plural': 'carga de imagenes masiva'},
        ),
        migrations.RemoveField(
            model_name='indexacion',
            name='resumen',
        ),
        migrations.AddField(
            model_name='indexacion',
            name='make_ocr',
            field=models.BooleanField(default=False, verbose_name=b'hacer ocr'),
            preserve_default=True,
        ),
    ]
