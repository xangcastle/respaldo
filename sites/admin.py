from django.contrib import admin
from recibos.models import Site
from models import site_equipo,site_inventario,site_requisa

class site_equipo_admin(admin.ModelAdmin):
    def get_queryset(self, request):
        sds = Site.objects.filter(encargado=request.user)
        le = []
        if sds:
            for s in sds:
                le += s.equipos.values_list('id',flat=True)
        ids = site_equipo.objects.filter(id__in=le).values_list('id',flat=True)
        qs = super(site_equipo_admin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id__in=ids)

admin.site.register(site_equipo,site_equipo_admin)
admin.site.register(site_inventario)
admin.site.register(site_requisa)
