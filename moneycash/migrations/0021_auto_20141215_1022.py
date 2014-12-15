# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0020_deposito_moneda'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factura',
            old_name='autorizada',
            new_name='autorizado',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='contabilizada',
            new_name='contabilizado',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='entregada',
            new_name='entregado',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='impresa',
            new_name='impreso',
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='autorizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='contabilizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='impreso',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposito',
            name='autorizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposito',
            name='contabilizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposito',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deposito',
            name='impreso',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibo',
            name='autorizado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibo',
            name='entregado',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='deposito',
            name='moneda',
            field=models.ForeignKey(related_name=b'moneycash_deposito_caja', default=1, to='moneycash.Moneda'),
        ),
    ]
