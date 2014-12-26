from recibos.models import Articulo
from django import template

register = template.Library()


class estadisticasNode(template.Node):
    def __init__(self, varname):
        self.varname = varname

    def __repr__(self):
        return "<GetInventario Node>"

    def render(self, context):
            context[self.varname] = Articulo.objects.all()
            return ''


@register.tag
def get_inventario(parser, token):
    """
        uso
            {% get_inventario as [varname]%}
    """
    tokens = token.contents.split()
    args = len(tokens)

    if not len(tokens) == 3:
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere de dos argumentos y se dieron %s"
            % (args))

    if not tokens[1] == 'as':
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere que el primer argumento sea 'as'")

    return estadisticasNode(varname=tokens[2])