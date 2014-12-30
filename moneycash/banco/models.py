from django.db import models


class cuenta(models.Model):
    nombre = models.ChartField(max_length=100)
    telefono = models.ChartField(max_length=15)
    deuda = models.FloatField()
    clase = models.ChartField(max_length=50)
    prestamo = models.FloatField()
    abonos = models.FloatField()