# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0003_auto_20150408_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('oficial', models.FloatField()),
                ('moneda', models.ForeignKey(default=1, to='moneycash.Moneda')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
