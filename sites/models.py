from recibos.models import Site as base_site, Articulo as base_articulo, Equipo as base_equipo, Requisa as base_requisa

class Site(base_site):
    class Meta:
        proxy = True
        
class Articulo(base_articulo):
    class Meta:
        proxy = True
        
class Equipo(base_equipo):
    class Meta:
        proxy = True
        
class Requisa(base_requisa):
    class Meta:
        proxy = True
