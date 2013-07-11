#encoding: utf-8
from django import template
from django.template.defaultfilters import stringfilter
from django import template
from django.core.urlresolvers import get_resolver
import re
from home.models import *
register = template.Library()

@register.simple_tag
def active(request, pattern):

    if re.search(pattern, request.path):
        return 'active'
    return ''

@register.simple_tag
def current(request, view):
    possible_results = get_resolver(None).reverse_dict.getlist(view)

    if len(possible_results) != 0 and re.match(possible_results[0][1], request.path[1:]):
        return 'current'
    return ''


@register.inclusion_tag('home/menu.html')
def middle_menu():
    top = MainPage.objects.filter(position=2, status=True).order_by('-order')
    return {'top': top,}


@register.inclusion_tag('home/content.html')
def middle_content():
    contents = MainPage.objects.filter(position=1, status=True).order_by('order')[:3]
    return {'contents': contents,}

