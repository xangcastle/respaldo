from moneycash.models import Banco as base_banco


class Banco(base_banco):
    class Meta:
        proxy = True

