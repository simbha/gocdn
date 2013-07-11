#encoding: utf-8
__author__ = 'jasmine'
from django.contrib import admin
from gocdn.home.models import *
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _


class HomeAdmin(admin.ModelAdmin):
    list_display = ['title','slug','photo','status','order','position']
    search_fields = ['title','slug','photo','status','order','position']
    ordering = ['-id']
    prepopulated_fields = {'slug' : ('title',)}

admin.site.register(MainPage, HomeAdmin)
admin.site.register(Positions)
admin.site.register(Customers)