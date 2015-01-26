from django.db.models import Manager
from .middlewares import get_current_user


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


class user_manager(Manager):
    def get_queryset(self):
        if str(get_current_user()) == 'AnonymousUser':
            return super(user_manager, self).get_queryset()
        else:
            return super(user_manager, self).get_queryset(
                ).filter(user=get_current_user())


class empresa_manager(Manager):
    def get_queryset(self):
        if str(get_current_user()) == 'AnonymousUser':
            return super(empresa_manager, self).get_queryset()
        else:
            if get_current_user().empresa:
                return super(empresa_manager, self).get_queryset(
                    ).filter(empresa=get_current_user().empresa)
            else:
                return super(empresa_manager, self).get_queryset()
