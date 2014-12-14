
from django.db.models import Q
from django.utils.html import escape
from ajax_select import LookupChannel
from moneycash.models import Cliente


class ClienteLookup(LookupChannel):

    model = Cliente

    def get_query(self, q, request):
        return Cliente.objects.filter(Q(name__icontains=q) | Q(code__istartswith=q)).order_by('name')

    def get_result(self, obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.name

    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return u"%s<div><i>%s</i></div><div><i>%s</i></div>" % (escape(obj.name), escape(obj.telefono), escape(obj.direccion))
        # return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"<a href=""/admin/moneycash/cliente/%s""onclick=""return showAddAnotherPopup(this);"">%s</a><div><i>%s</i></div><div><i>%s</i></div>" % (escape(obj.id), escape(obj.name), escape(obj.telefono), escape(obj.direccion))

