import autocomplete_light
from .models import Item

autocomplete_light.register(Item,
    search_fields=['^code', 'name'],
    attrs={
        'data-autocomplete-minimum-characters': 2,
    },
    widget_attrs={
        'data-widget-maximum-values': 10,
        'class': 'modern-style',
    },
)
