from django.views.generic.base import TemplateView
import json
from django.http.response import HttpResponse
from .models import *


class verificacion_paquete(TemplateView):
    template_name = "metropolitana/verificacion.html"


def datos_paquete(request):

    if request.method == 'GET':
        p = Paquete()
        try:
            p = Paquete.objects.get(barra=request.GET.get('barra', ''))
            datos = {'cliente': p.cliente, 'departamento': p.departamento,
                'municipio': p.municipio, 'lote': p.lote.numero}
        except p.DoesNotExist:
            datos = {'cliente': 'nada'}
        resp =  HttpResponse(json.dumps(datos), content_type='application/json')
        resp["Access-Control-Allow-Origin"] = "*"
        resp["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        resp["Access-Control-Allow-Headers"] = "X-Requested-With"
        return resp
    else:
        datos = {'nombre': 'nada'}
        resp = HttpResponse(json.dumps(datos),
            content_type='application/json')
        resp["Access-Control-Allow-Origin"] = "*"
        resp["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        resp["Access-Control-Allow-Headers"] = "X-Requested-With"
        return resp


########################################################
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string


def generar_pdf(html):
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


def comprobantes_pdf(request, id):
    queryset = Lote.objects.filter(id__in=id)
    html = render_to_string('metropolitana/comprobante.html',
        {'pagesize': 'A4', 'queryset': queryset},
        context_instance=RequestContext(request))
    return generar_pdf(html)



