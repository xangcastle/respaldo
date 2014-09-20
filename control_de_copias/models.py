from recibos.models import Recibo,Periodo
from django.db import models

class recibo_manager(models.Manager):
    def get_queryset(self):
        periodos = Periodo.objects.filter(cerrado=False).values_list('id',flat=True).order_by('id')
        return super(recibo_manager,self).get_queryset().filter(periodo__in=periodos)

class recibo(Recibo):
    objects = models.Manager()
    objects = recibo_manager()
    class Meta:
        proxy = True
