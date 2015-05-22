from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from ajax_select import urls as ajax_select_urls
from django.contrib import admin
import autocomplete_light
from home.views import *
#import reporting


autocomplete_light.autodiscover()
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    #url(r'^$', 'recibos.views.principal', name='principal'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Admin timeline URLs. Should be placed BEFORE the Django admin URLs.
    #(r'^admin/timeline/', include('admin_timeline.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^adminactions/', include('adminactions.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^entregas/', include('metropolitana.urls')),
    url(r'^imprimir/', include('moneycash.contabilidad.urls')),
    #url(r'^reporting/', include(reporting.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
