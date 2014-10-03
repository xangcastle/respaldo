from recibos.models import Recibo,Periodo
from django.db import models

class produccion_manager(models.Manager):
    def get_query_set(self):
        periodos = Periodo.objects.filter(cerrado=False)
        return super(produccion_manager,self).get_query_set().filter(periodo__in=periodos)

class produccion_equipo(Recibo):
    objects = models.Manager()
    objects = produccion_manager()
    class Meta:
        proxy = True
        verbose_name = "equipo"
        verbose_name_plural = "equipos en produccion"
