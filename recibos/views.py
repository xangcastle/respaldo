from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from models import Equipo,Periodo,Recibo,Area
from datetime import datetime

def principal(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def equipos(request):
    equipos = Equipo.objects.filter(activo=True).order_by('area')
    ctx = {'equipos':equipos}
    return render_to_response('recibos/equipos.html',ctx,context_instance=RequestContext(request))


def recibo(request,id_equipo):
    recibo = Recibo.objects.get(periodo=Periodo.objects.get(cerrado=False),equipo=Equipo.objects.get(id=id_equipo))
    ctx = {'recibo':recibo}
    return render_to_response('recibos/impreso.html',ctx,context_instance=RequestContext(request))

def cuadro(request):
    periodo = Periodo.objects.get(cerrado=False)
    recibos = Recibo.objects.filter(periodo=periodo)
    ctx = { 'recibos':recibos, 'periodo':periodo }
    return render_to_response('recibos/cuadro.html',ctx,context_instance=RequestContext(request))

def recibo_add(request,id_equipo):
    equipo = Equipo.objects.get(id = id_equipo)
    periodo = Periodo.objects.filter(cerrado=False)[0]
    recibo = Recibo()
    recibo.equipo = equipo
    recibo.periodo = periodo
    recibo.contador_inicial = equipo.contador
    areas = equipo.areas.all()
    info = "iniciado"
    etiqueta = 'Control de Impresiones'
    if request.method == "POST":
        form = ReciboForm(request.POST,request.FILES)
        if form.is_valid():
            recibo.contador_final = form.cleaned_data['contador_final']
            recibo.save()
            equipo.contador = recibo.contador_final
            equipo.save()
            info = "Guardado satisfactoriamente"
            return HttpResponseRedirect('/rentas/recibos/%s'%recibo.id)
    else:
        form = ReciboForm(initial={
                                    'marca':recibo.equipo.marca,
                                    'modelo':recibo.equipo.modelo,
                                    'serie':recibo.equipo.serie,
                                    'contador_inicial':recibo.equipo.contador,
                                    'fecha_inicial':recibo.periodo.fecha_inicial,
                                    'fecha_final':recibo.periodo.fecha_final,
                                    'contador_final':0,
            })
        
    ctx = {'form':form,'informacion':info,'equipo':equipo,'areas':areas,'etiqueta':etiqueta}
    return render_to_response('recibos/add.html',ctx,context_instance=RequestContext(request))
def recibo2(request,id_rec):
    recibo = Recibo.objects.get(id=id_rec)
    form = ReciboForm(initial={
                                    'marca':recibo.equipo.marca,
                                    'modelo':recibo.equipo.modelo,
                                    'serie':recibo.equipo.serie,
                                    'contador_inicial':recibo.equipo.contador,
                                    'fecha_inicial':recibo.periodo.fecha_inicial,
                                    'fecha_final':recibo.periodo.fecha_final,
                                    'contador_final':0,
            })
    ctx = {'recibo':recibo,'form':form}
    return render_to_response('recibos/single.html',ctx,context_instance=RequestContext(request))

def toners(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def recibos(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def InsToner_add(request,id_equipo):
    equipo  = Equipo.objects.get(id = id_equipo)
    periodo = Periodo.objects.filter(cerrado=False)[0]
    instoner = InsToner()
    instoner.equipo = equipo
    instoner.periodo = periodo
    instoner.fecha = datetime.now()
    instoner.contador = equipo.contador
    etiqueta = 'Control de Instalacion de Toner'
    if request.method == 'POST':
        form = InsTonerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rentas/toners/%s'%instoner.id)
    else:
        form = InsTonerForm(instance=instoner)
    ctx = {'form':form,'etiqueta':etiqueta}
    return render_to_response('recibos/add.html',ctx,context_instance=RequestContext(request))

def Mantenimiento_add(request,id_equipo):
    equipo  = Equipo.objects.get(id = id_equipo)
    periodo = Periodo.objects.filter(cerrado=False)[0]
    instoner = InsToner()
    instoner.equipo = equipo
    instoner.periodo = periodo
    instoner.fecha = datetime.now()
    instoner.contador = equipo.contador
    etiqueta = 'Control de Instalacion de Toner'
    if request.method == 'POST':
        form = InsTonerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rentas/toners/%s'%instoner.id)
    else:
        form = InsTonerForm(instance=instoner)
    ctx = {'form':form,'etiqueta':etiqueta}
    return render_to_response('recibos/add.html',ctx,context_instance=RequestContext(request))