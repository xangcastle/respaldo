from django.db.models import Manager


# ESTADOS DE DOCUMENTOS
class documento_autorizado(Manager):
    def get_queryset(self):
        return super(documento_autorizado, self).get_queryset().filter(
            autorizado=True)


class documento_no_autorizado(Manager):
    def get_queryset(self):
        return super(documento_no_autorizado, self).get_queryset().filter(
            autorizado=False)


class documento_impreso(documento_autorizado):
    def get_queryset(self):
        return super(documento_impreso, self).get_queryset().filter(
            impreso=True)


class documento_no_impreso(documento_autorizado):
    def get_queryset(self):
        return super(documento_no_impreso, self).get_queryset().filter(
            impreso=False)


class documento_entregado(documento_impreso):
    def get_queryset(self):
        return super(documento_entregado, self).get_queryset().filter(
            entregado=True)


class documento_no_entregado(documento_impreso):
    def get_queryset(self):
        return super(documento_no_entregado, self).get_queryset().filter(
            entregado=False)


class documento_contabilizado(documento_impreso):
    def get_queryset(self):
        return super(documento_contabilizado, self).get_queryset().filter(
            contabilizado=True)


class documento_no_contabilizado(documento_impreso):
    def get_queryset(self):
        return super(documento_no_contabilizado, self).get_queryset().filter(
            contabilizado=False)