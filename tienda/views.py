from django.shortcuts import render_to_response
from django.template import RequestContext


def TiendaPageView(request):
    template_name = "tienda/tienda.html"
    data = []
    context = RequestContext(request)
    return render_to_response(template_name, data, context_instance=context)
