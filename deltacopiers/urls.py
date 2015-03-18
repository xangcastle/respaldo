from django.conf.urls import patterns, include, url
from ajax_select import urls as ajax_select_urls
from django.contrib import admin
import autocomplete_light
from home.views import *


autocomplete_light.autodiscover()
admin.autodiscover()
#djadmin2.default.autodiscover()


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    #url(r'^$', 'recibos.views.principal', name='principal'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Admin timeline URLs. Should be placed BEFORE the Django admin URLs.
    #(r'^admin/timeline/', include('admin_timeline.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^deltacopiers/', include('recibos.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
