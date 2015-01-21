from moneycash.models import Banco as base_banco, Moneda as base_moneda, \
tipo_movimiento as base_tipo_movimiento, Cuenta_Banco as base_cuenta_banco, \
tipo_cambio as base_tasa_cambio


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


class Cuenta_Banco(base_cuenta_banco):
    class Meta:
        proxy = True
        verbose_name = "cuenta de banco"
        verbose_name_plural = "cuentas de bancos"


class tipo_cambio(base_tasa_cambio):
    class Meta:
        proxy = True
        verbose_name = "cuenta de banco"
        verbose_name_plural = "cuentas de bancos"