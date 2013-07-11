#encoding: utf-8

from django import template
from django.db.models import Q, F
from django.db.models.loading import get_model
from datetime import datetime, timedelta
from django.forms.models import model_to_dict
from decimal import Decimal
from django.core.cache import cache
from gostream.general.models import Menu
from django.template.loader import add_to_builtins

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def menu(context):
    menu = Menu.objects.all().order_by('menu_order')
    return {'menu':menu}



