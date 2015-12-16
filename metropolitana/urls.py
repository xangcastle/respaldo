# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('metropolitana.views',
    url(r'^verificacion/$', verificacion_paquete.as_view(),
        name='verificacion_paquete'),
    url(r'^entrega/$', entrega_paquete.as_view(),
        name='entrega_paquete'),
    url(r'^datospaquete/$', 'datos_paquete', name='datos_paquete'),
    url(r'^indexar/$', indexar.as_view(), name='indexar'),
    url(r'^descarga/$', 'descarga', name='descarga'),
)