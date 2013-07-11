#encoding: utf-8
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='custom_app_label')
@stringfilter
def custom_app_label(value):
    custom_app_labels = {
        'Auth': 'Accounts', # key is default app_label, value is new app_label
        # Rinse, repeat
        'Members':'kullanıcılar'
    }
    return custom_app_labels.get(value, value)
