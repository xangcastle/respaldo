# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('metropolitana.views',
    url(r'^verificacion/$', verificacion_paquete.as_view(),
        name='verificacion_paquete'),
    url(r'^datospaquete/$', 'datos_paquete', name='datos_paquete'),
    url(r'^comprobantespdf/$', 'comprobantes_pdf', name='comprobantes_pdf'),
)