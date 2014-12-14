try:
    from example.music import *
except:
    from example.music import *
from example.music import static
from example.music import admin
from example.music import settings
from example.music import urls as ajax_select_urls


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^search_form',  view='example.views.search_form', name='search_form'),
    (r'^admin/lookups/', include(ajax_select_urls)),
    (r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
