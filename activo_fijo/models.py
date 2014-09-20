from recibos.models import Equipo,Marca
class equipo(Equipo):
    class Meta:
        proxy = True
class marca(Marca):
    class Meta:
        proxy = True

