from django.contrib.sites.models import Site
from django import template

register = template.Library()


@register.simple_tag
def get_hostname():
    current_site = Site.objects.get_current()
    return current_site.domain
