from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Periodo,Recibo

def principal(request):
    return HttpResponseRedirect('/admin')

def recibo(request,id_recibo):
    recibo = Recibo.objects.get(id=id_recibo)
    ctx = {'recibo':recibo}
    return render_to_response('recibos/impreso.html',ctx,context_instance=RequestContext(request))

def cuadro(request,id_periodo):
    periodo = Periodo.objects.get(id=id_periodo)
    recibos = Recibo.objects.filter(periodo=periodo)
    ctx = { 'recibos':recibos, 'periodo':periodo }
    return render_to_response('recibos/cuadro.html',ctx,context_instance=RequestContext(request))
