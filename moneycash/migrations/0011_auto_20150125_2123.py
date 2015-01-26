# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneycash', '0010_empresa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bodega',
            options={},
        ),
        migrations.AlterModelOptions(
            name='caja',
            options={},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cuenta',
            options={},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={},
        ),
        migrations.AddField(
            model_name='bodega',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_bodega_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='caja',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_caja_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categoria',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_categoria_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cierrecaja',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_cierrecaja_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_cliente_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_compra_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contacto',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_contacto_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cuenta',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_cuenta_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle_pago',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_detalle_pago_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallecompra',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_detallecompra_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detallepoliza',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_detallepoliza_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_factura_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_factura_detalle_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_item_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='marca',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_marca_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='poliza',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_poliza_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provedor',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_provedor_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recibo',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_recibo_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sucursal',
            name='empresa',
            field=models.ForeignKey(related_name=b'moneycash_sucursal_empresa', to='moneycash.Empresa', null=True),
            preserve_default=True,
        ),
    ]
