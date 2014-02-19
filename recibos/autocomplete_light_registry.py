import autocomplete_light
from models import Item

autocomplete_light.register(Item,
    search_fields=['no_parte','nombre'],
    autocomplete_js_attributes={'placeholder': 'ITEM',},
)
