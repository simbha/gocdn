#encoding: utf-8
__author__ = 'yasemen karakoc'
from django.contrib import admin
from gocdn.general.models import *
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _
from gocdn.helpdesk.models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']
    ordering = ['order']

class HelpAdmin(admin.ModelAdmin):
    list_display = ['help_title','help_user','help_subject','help_content']
    ordering = ['-id']
    search_fields = ['help_title','help_user','help_subject','help_content']


admin.site.register(Help, HelpAdmin)
admin.site.register(HelpSubject, SubjectAdmin)

