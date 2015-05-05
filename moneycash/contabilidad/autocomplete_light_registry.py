# -*- coding: utf-8 -*-
import autocomplete_light
from .models import *


autocomplete_light.register(Cuenta,
    search_fields=['^code', 'name'],
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'nombre o numero de cuenta',
    },
    widget_attrs={
        'data-widget-maximum-values': 10,
        'class': 'modern-style',
    },
)


autocomplete_light.register(Operativa,
    search_fields=['^code', 'name'],
    attrs={
        'data-autocomplete-minimum-characters': 2,
        'placeholder': 'nombre o numero de cuenta',
    },
    widget_attrs={
        'data-widget-maximum-values': 10,
        'class': 'modern-style',
    },
)
