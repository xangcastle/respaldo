from django.contrib import admin
from recibos.models import Site
from models import Equipo,Articulo,Requisa

class site_equipo_admin(admin.ModelAdmin):
    def get_queryset(self, request):
        sds = Site.objects.filter(encargado=request.user)
        le = []
        if sds:
            for s in sds:
                le += s.equipos.values_list('id',flat=True)
        ids = Equipo.objects.filter(id__in=le).values_list('id',flat=True)
        qs = super(site_equipo_admin, self).get_queryset(request)
        
        return qs.filter(id__in=ids)

admin.site.register(Equipo,site_equipo_admin)
admin.site.register(Articulo)
admin.site.register(Requisa)
