from moneycash.models import Banco as base_banco, Moneda as base_moneda, \
tipo_movimiento as base_tipo_movimiento


class Banco(base_banco):
    class Meta:
        proxy = True


class Moneda(base_moneda):
    class Meta:
        proxy = True


class tipo_movimiento(base_tipo_movimiento):
    class Meta:
        proxy = True
        verbose_name = "tipo de transaccion"
        verbose_name_plural = "tipos de transacciones"