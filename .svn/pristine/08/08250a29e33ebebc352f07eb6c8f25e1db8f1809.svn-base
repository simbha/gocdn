#encoding: utf-8
__author__ = 'jasmine'
from django.contrib import admin
from gocdn.faq.models import *
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _

class FaqAdmin(admin.ModelAdmin):

    list_display = ['question','answer','status','sort_order']
    search_fields = ['question','answer','status','sort_order']
    list_filter = ['question','answer','status','sort_order']
    ordering = ['-id']
    prepopulated_fields = {'slug' : ('question',)}
    list_editable = ['status']



admin.site.register(Faqs, FaqAdmin)
