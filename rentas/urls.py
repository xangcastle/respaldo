from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','recibos.views.principal',name='principal'),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rentas/', include('recibos.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
)
