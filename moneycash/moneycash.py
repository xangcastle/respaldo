# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Max


def get_code(modelo):
        model = type(modelo)
        code = 1
        sets = model.objects.all()
        if sets:
            maxi = sets.aggregate(Max('code'))['code__max']
            if maxi:
                consecutivo = list(range(1, maxi))
                ocupados = list(sets.values_list('code',
                flat=True))
                disponibles = list(set(consecutivo) - set(ocupados))
                if len(disponibles) > 0:
                    code = min(disponibles)
                else:
                    code = max(ocupados) + 1
        return str(code).zfill(4)


class entidad(models.Model):
    code = models.CharField(max_length=25, null=True, blank=True,
        verbose_name="codigo")
    name = models.CharField(max_length=100, verbose_name="nombre")
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        if self.code and self.name:
            return str(self.code) + " " + self.name
        elif self.name:
            return self.name
        elif self.code:
            return str(self.code)
        else:
            return ''

    def save(self, *args, **kwargs):
        if self.code is None or self.code == '':
            self.code = get_code(self)
        super(entidad, self).save()

    class Meta:
        abstract = True
        ordering = ['name']
