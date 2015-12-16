from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from ajax_select import urls as ajax_select_urls
from django.contrib import admin
from home.views import *


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    #url(r'^$', 'recibos.views.principal', name='principal'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^adminactions/', include('adminactions.urls')),
    url(r'^entregas/', include('metropolitana.urls')),
    url(r'^imprimir/', include('moneycash.contabilidad.urls')),
    url(r'^produccion/', include('moneycash.produccion.urls')),
    url(r'^movil/', include('movil.urls')),
    url(r'^quickdocs/', include('quickdocs.urls')),
    url(r'^digitalizacion/', include('digitalizacion.urls')),
    url(r'^tienda/', include('tienda.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
