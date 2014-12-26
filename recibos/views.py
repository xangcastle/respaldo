from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Periodo, Recibo


def principal(request):
    return HttpResponseRedirect('/admin')


def cuadro(request, id_periodo):
    periodo = Periodo.objects.get(id=id_periodo)
    recibos = Recibo.objects.filter(periodo=periodo)
    ctx = {'recibos': recibos, 'periodo': periodo}
    return render_to_response('recibos/cuadro.html', ctx,
        context_instance=RequestContext(request))
