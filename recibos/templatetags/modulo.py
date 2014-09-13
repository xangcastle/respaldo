from recibos.models import Recibo,Periodo
from django import template

register = template.Library()

@register.simple_tag
def get_estadisticas():
    recibos = Recibo.objects.filter(periodo__in=Periodo.objects.filter(cerrado=False))
    if recibos:
        return recibos
    else:
        return None