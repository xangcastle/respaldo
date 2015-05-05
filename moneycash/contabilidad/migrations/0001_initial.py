# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balanza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saldo_inicial', models.FloatField(default=0)),
                ('saldo_final', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=25, null=True, verbose_name=b'codigo', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nombre')),
                ('activo', models.BooleanField(default=True)),
                ('saldo', models.FloatField(default=0, help_text=b'saldo actual de la cuenta')),
                ('cuenta', models.ForeignKey(related_name='cuenta_madre', blank=True, to='contabilidad.Cuenta', null=True)),
            ],
            options={
                'ordering': ['code'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicial', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
            options={
                'ordering': ['-fecha_final'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='balanza',
            name='cuenta',
            field=models.ForeignKey(to='contabilidad.Cuenta'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='balanza',
            name='periodo',
            field=models.ForeignKey(to='contabilidad.Periodo'),
            preserve_default=True,
        ),
    ]
