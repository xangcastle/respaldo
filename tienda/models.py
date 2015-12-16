from django.db import models


class Articulo(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=250)
    precio = models.FloatField()
    existencia = models.FloatField()
    imagen = models.FileField(upload_to="tienda")

    def __unicode__(self):
        return self.nombre