from recibos.models import Recibo,Periodo
from django import template

register = template.Library()

class estadisticasNode(template.Node):
    def __init__(self, varname):
        self.varname

    def __repr__(self):
        return "<GetEstadisticas Node>"

    def render(self, context):
            context[self.varname] = Recibo.objects.filter(periodo__in=Periodo.objects.filter(cerrado=False))
            return ''

@register.tag
def get_estadisticas(parser, token):
    """
        uso
            {% get_estadisticas as [varname]%}
    """
    tokens = token.contents.split()
    args = len(tokens)
    
    if not len(tokens) == 2:
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere de dos argumentos y se dieron %s" % (args))
    if not tokens[2]=='as':
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere que el primer argumento se 'as'")
        
    return estadisticasNode(varname=tokens[2])