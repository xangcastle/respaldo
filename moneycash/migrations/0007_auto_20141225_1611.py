# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0006_auto_20141219_0214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banco',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='bodega',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='caja',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='moneda',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='pago',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='provedor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='serie',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tipocosto',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='banco',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='banco',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='caja',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='caja',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='identificacion',
            field=models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='moneda',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='provedor',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='provedor',
            name='identificacion',
            field=models.CharField(max_length=25, null=True, verbose_name=b'ruc/cedula', blank=True),
        ),
        migrations.AlterField(
            model_name='provedor',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='provedor',
            name='tiempo_entrega',
            field=models.PositiveIntegerField(default=0, help_text=b'tiempo de entrega en dias para la mercaderia', verbose_name=b'tiempo de entrega'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
        migrations.AlterField(
            model_name='tipocosto',
            name='code',
            field=models.CharField(max_length=25, verbose_name=b'codigo'),
        ),
        migrations.AlterField(
            model_name='tipocosto',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'nombre'),
        ),
    ]
