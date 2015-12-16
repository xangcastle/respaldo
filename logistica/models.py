from django.db import models
from metropolitana.models import Entidad, get_media_url


class Departamento(Entidad):
    codigo_telefonico = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = 'metropolitana_barrio'


class Municipio(Entidad):
    departamento = models.ForeignKey(Departamento, null=True, blank=True)

    class Meta:
        db_table = 'metropolitana_municipio'


class Barrio(Entidad):
    departamento = models.ForeignKey(Departamento, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, null=True, blank=True)

    class Meta:
        db_table = 'metropolitana_barrio'


class Colector(Entidad):
    foto = models.FileField(upload_to=get_media_url, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'colectores'
        db_table = 'metropolitana_colector'


class Ruta(Entidad):
    class Meta:
        verbose_name_plural = "rutas de distribucion"