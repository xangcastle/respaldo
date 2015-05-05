from django.db import models
from moneycash.models import Entidad


class Usuario(Entidad):
    user = models.CharField(max_length=25)
    grupo = models.ForeignKey('Grupo')
    agencias = models.ForeignKey('Agencia')


class Grupo(Entidad):
    pass


class Agencia(Entidad):
    pass