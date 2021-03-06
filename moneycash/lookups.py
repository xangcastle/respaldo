from django.db.models import Q
from django.utils.html import escape
from ajax_select import LookupChannel
from .models import Cliente, Item, Provedor
from .middlewares import get_current_user
from django.core.urlresolvers import reverse


class ClienteLookup(LookupChannel):

    model = Cliente

    def get_query(self, q, request):
        return Cliente.objects.filter(
            Q(name__icontains=q) | Q(code__istartswith=q)).order_by('name')

    def get_result(self, obj):
        return obj.name

    def format_match(self, obj):
        return "%s<div><i>%s</i></div><div><i>%s</i></div>"\
        % (escape(obj.name), escape(obj.telefono), escape(obj.direccion))
        # return self.format_item_display(obj)

    def format_item_display(self, obj):
        return "<div class=""grp-row grp-cells-1 name ""><div class=""l-2c-fluid l-d-4""><div class=""c-1""><label>Name</label></div><div class=""c-2""><div class=""grp-readonly"">%s</div></div></div></div><div class=""grp-row grp-cells-1 code ""><div class=""l-2c-fluid l-d-4""><div class=""c-1""><label>Code</label></div><div class=""c-2""><div class=""grp-readonly"">%s</div></div></div></div><div class=""grp-row grp-cells-1 identificacion ""><div class=""l-2c-fluid l-d-4""><div class=""c-1""><label>Identificacion</label></div><div class=""c-2""><div class=""grp-readonly"">%s</div></div></div></div><div class=""grp-row grp-cells-1 telefono ""><div class=""l-2c-fluid l-d-4""><div class=""c-1""><label>Telefono</label></div><div class=""c-2""><div class=""grp-readonly"">%s</div></div></div></div><div class=""grp-row grp-cells-1 direccion ""><div class=""l-2c-fluid l-d-4""><div class=""c-1""><label>Direccion</label></div><div class=""c-2""><div class=""grp-readonly"">%s</div></div></div></div>"\
        % (escape(obj.name), escape(obj.code),
            escape(obj.identificacion), escape(obj.telefono),
            escape(obj.direccion))


class ItemLookup(LookupChannel):

    model = Item

    def get_query(self, q, request):
        return Item.objects.filter(
            Q(name__icontains=q) | Q(code__istartswith=q)).order_by('name')

    def get_result(self, obj):
        return obj.name

    def format_match(self, obj):
        return "%s<div><i>%s</i></div><div><i>%s</i></div><div><i>%s</i></div>"\
        % (escape(obj.name), escape(obj.precio),
        escape(obj.costo), escape(obj.existencias))

    def format_item_display(self, obj):
        return "<a href=""/admin/moneycash/item/%s"">%s</a><div><i>precio = %s</i></div><div><i>costo = %s</i></div><div><i>existencias = %s</i></div>"\
        % (escape(obj.id), escape(obj.name),
        escape(obj.precio), escape(obj.costo),
        escape(obj.existencias))