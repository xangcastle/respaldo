#-*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django.db.models.loading import get_model


class Node(object):
    pass


class CLNode(Node):
    def __init__(self, app, model, title=None, perms=['change']):
        self.app = app
        self.model = model
        self.title = title
        self.perms = perms

    def as_tuple(self):
        model = get_model(self.app, self.model)
        vnp = model._meta.verbose_name_plural
        if self.title is None:
            title = \
                self.model.title() + 's' if vnp == self.model + 's' else vnp
        else:
            title = self.title
        perms = ['%s.%s_%s' % (self.app, i, self.model) for i in self.perms]
        return title, {
            'perms': perms,
            'url': reverse('admin:%s_%s_changelist' % (self.app, self.model))}
