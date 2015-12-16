# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import metropolitana.models


class Migration(migrations.Migration):

    dependencies = [
        ('metropolitana', '0005_paquete_orden_impresion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='impresion',
            options={'ordering': ['consecutivo'], 'verbose_name_plural': 'impresiones'},
        ),
        migrations.RenameField(
            model_name='paquete',
            old_name='iddepartemento',
            new_name='iddepartamento',
        ),
        migrations.AlterField(
            model_name='paquete',
            name='comprobante',
            field=models.FileField(null=True, upload_to=metropolitana.models.generar_ruta_comprobante, blank=True),
            preserve_default=True,
        ),
    ]
