from moneycash.models import Banco as base_banco, Moneda as base_moneda


class Banco(base_banco):
    class Meta:
        proxy = True


class Moneda(base_moneda):
    class Meta:
        proxy = True
