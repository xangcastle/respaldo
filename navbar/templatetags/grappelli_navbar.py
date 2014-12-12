 #-*- coding:utf-8 -*-

import sys

from django import template
from django.conf import settings
from django.templatetags.static import static

from classytags.core import Tag, Options
from classytags.helpers import InclusionTag

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import capfirst

site = admin.site


def get_extension(setting, default, *args, **kwargs):
    extension = getattr(settings, setting, default)
    parts = extension.split(".")
    module = ".".join(parts[:-1])
    __import__(module)
    module = sys.modules[module]
    return getattr(module, parts[-1])


def applist(request):
    app_dict = {}
    user = request.user
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        has_module_perms = user.has_module_perms(app_label)
        
        if has_module_perms:
            perms = model_admin.get_model_perms(request)
            
            if True in perms.values():
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'admin_url': mark_safe('/admin/%s/%s/' % (app_label, model.__name__.lower())),
                    'perms': perms,
                }
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    app_dict[app_label] = {
                        'name': app_label.title(),
                        'app_url': app_label + '/',
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }
                    
    app_list = app_dict.values()
    app_list.sort(lambda x, y: cmp(x['name'], y['name']))
    return app_list


def get_navbar():
    return get_extension('GRAPPELLI_EXTENSIONS_NAVBAR',
                         'grappelli_extensions.navbar.Navbar')


def get_sidebar():
    return get_extension('GRAPPELLI_EXTENSIONS_SIDEBAR',
                         'grappelli_extensions.navbar.Navbar')


def get_theme():
    return getattr(settings, 'GRAPPELLI_THEME', None)


def has_perms(request, params):
    if 'perm' in params:
        perms = [params['perm']]
    else:
        perms = params.get('perms', [])
    if perms:
        perms = [request.user.has_perm(p) for p in perms]
        return any(perms)
    return True


def get_children(Navbar, request):
    children = []
    for node in Navbar.nodes:
        if node.__class__.__name__.endswith("Node"):
            title, params = node.as_tuple()
        else:
            title, params = node

        if not has_perms(request, params):
            continue

        nodes = params.get("nodes", [])
        url = params.get('url')
        root = {'title': title, 'children': [], 'url': url}
        for node in nodes:
            if node.__class__.__name__.endswith("Node"):
                title, params = node.as_tuple()
            else:
                title, params = node

            url = params.get('url')
            node = {'title': title, 'url': url}
            if has_perms(request, params):
                root['children'].append(node)

        if root['children'] or root['url']:
            children.append(root)
    return children


class GrappelliNavbar(InclusionTag):
    name = 'grappelli_navbar'
    template = 'grappelli/navbar.html'

    def get_context(self, context):
        navbar = get_navbar()
        menu = applist(context['request'])
        return {'children': get_children(navbar, context['request']),'apps':menu}
    


class GrappelliSidebar(InclusionTag):
    name = 'grappelli_sidebar'
    template = 'grappelli/sidebar.html'

    def get_context(self, context):
        sidebar = get_sidebar()
        return {
            'sidebar_children': get_children(sidebar, context['request']),
            'request': context['request']
        }


class GrappelliHasSidebar(Tag):
    name = 'grappelli_has_sidebar'
    options = Options(
        blocks=[('endsidebar', 'nodelist')],
    )

    def render_tag(self, context, nodelist):
        output = ''
        sidebar = get_sidebar()
        if len(sidebar.nodes):
            output = nodelist.render(context)
        return output


class GrappelliTheme(Tag):
    name = 'grappelli_theme'

    def render_tag(self, context):
        theme = get_theme()
        if not theme:
            return ''

        theme_static_url = static('css/%s.css' % (theme, ))
        output = '<link href=%s rel="stylesheet" type="text/css"\
                 media="screen" />' % (theme_static_url, )
        return output


register = template.Library()
register.tag(GrappelliNavbar)
register.tag(GrappelliSidebar)
register.tag(GrappelliHasSidebar)
register.tag(GrappelliTheme)
