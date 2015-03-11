# -*- coding: utf-8 -*-
from import_export import resources
from .models import Provedor


class provedor_resource(resources.ModelResource):
    class Meta:
        model = Provedor