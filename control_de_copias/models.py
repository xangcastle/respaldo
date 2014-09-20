from recibos.models import Recibo
from django.db import models

class recibo_manager(models.Manager):
    pass

class recibo(Recibo):
    class Meta:
        proxy = True
