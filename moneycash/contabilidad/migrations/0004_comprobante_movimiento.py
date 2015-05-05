# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0003_cuenta_naturaleza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('debe', models.FloatField(default=0)),
                ('haber', models.FloatField(default=0)),
                ('comprobante', models.ForeignKey(to='contabilidad.Comprobante')),
                ('cuenta', models.ForeignKey(to='contabilidad.Cuenta')),
                ('periodo', models.ForeignKey(to='contabilidad.Periodo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
