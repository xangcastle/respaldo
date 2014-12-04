# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recibos', '0010_fcompra_moneda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('comprar', models.BooleanField(default=True)),
                ('vender', models.BooleanField(default=True)),
                ('almacenar', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='refaccion',
            name='categoria',
            field=models.ForeignKey(to='recibos.Categoria', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provedor',
            name='nombre',
            field=models.CharField(max_length=100, null=True, verbose_name='nombre o razon social', blank=True),
        ),
    ]
