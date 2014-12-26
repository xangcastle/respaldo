from django.conf.urls import patterns, include, url
from ajax_select import urls as ajax_select_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'recibos.views.principal', name='principal'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^deltacopiers/', include('recibos.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
)
