from recibos.models import Site, Articulo, Equipo, Requisa

class site(Site):
    class Meta:
        proxy = True
        
class site_inventario(Articulo):
    class Meta:
        proxy = True
        verbose_name = "articulo"
        verbose_name_plural = "inventario"
        
class site_equipo(Equipo):
    class Meta:
        proxy = True
        
class site_requisa(Requisa):
    class Meta:
        proxy = True
        verbose_name = "requisa"
