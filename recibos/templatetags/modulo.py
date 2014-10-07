from recibos.models import Recibo,Periodo,Equipo
from django import template

register = template.Library()

class estadisticasNode(template.Node):
    def __init__(self, varname):
        self.varname = varname

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
    
    if not len(tokens) == 3:
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere de dos argumentos y se dieron %s" % (args))
    if not tokens[1]=='as':
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere que el primer argumento se 'as'")
        
    return estadisticasNode(varname=tokens[2])

class estadisticas_all_Node(template.Node):
    def __init__(self, varname):
        self.varname = varname

    def __repr__(self):
        return "<GetEstadisticas Node>"

    def render(self, context):
            context[self.varname] = Recibo.objects.filter(equipo__in=Equipo.objects.filter(activo=True))
            return ''

@register.tag
def get_estadisticas_all(parser, token):
    """
        uso
            {% get_estadisticas as [varname]%}
    """
    tokens = token.contents.split()
    args = len(tokens)
    
    if not len(tokens) == 3:
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere de dos argumentos y se dieron %s" % (args))
    if not tokens[1]=='as':
        raise template.TemplateSyntaxError(
            "'get_estadisticas' requiere que el primer argumento se 'as'")
        
    return estadisticas_all_Node(varname=tokens[2])