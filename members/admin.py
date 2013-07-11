#encoding: utf-8
__author__ = 'jasmine'
from django.contrib import admin
from gocdn.members.models import *
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _

class GoUserAdmin(admin.ModelAdmin):

    list_display = ['username','user_type','last_update']
    ordering = ['-id']
    search_fields = ['username','user_type', 'activation_code']


admin.site.register(GoUser, GoUserAdmin)