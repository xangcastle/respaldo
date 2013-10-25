from django.conf.urls import patterns, include, url

urlpatterns = patterns('recibos.views',
    url(r'^$','principal',name='principal'),
    url(r'^equipos/$','equipos',name='equipos'),
    url(r'^recibo/(?P<id_equipo>.*)/$','recibo',name='recibo'),
    url(r'^cuadro/$','cuadro',name='cuadro'),
    url(r'^recibo/add/(?P<id_equipo>.*)/$','recibo_add',name='Nuevo Recibo'),
    url(r'^recibos/(?P<id_rec>.*)/$','recibo',name='recibo'),
    url(r'^toners/$','equipos',name='toners'),
    url(r'^toner/add/(?P<id_equipo>.*)/$','InsToner_add',name='Nuevo Toner'),
    url(r'^mantenimiento/add/(?P<id_equipo>.*)/$','InsToner_add',name='Nuevo Toner'),
)
