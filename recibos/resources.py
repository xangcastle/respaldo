from import_export import resources
from models import Item

class Item_resouce(resources.ModelResource):
    class Meta:
        model = Item
