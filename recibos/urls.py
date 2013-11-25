from django.conf.urls import patterns, url

urlpatterns = patterns('recibos.views',
    url(r'^recibo/(?P<id_recibo>.*)/$','recibo',name='recibo'),
    url(r'^cuadro/(?P<id_periodo>.*)/$','cuadro',name='cuadro'),
)
