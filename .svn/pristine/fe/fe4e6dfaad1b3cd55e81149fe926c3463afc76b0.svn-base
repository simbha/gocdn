#encoding: utf-8
__author__ = 'jasmine'
from django.contrib import admin
from gocdn.tvstream.models import *
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _


class StreamerTypesAdmin(admin.ModelAdmin):

    ordering = ['-type_order']
    search_fields = ['type']
admin.site.register(StreamerTypes, StreamerTypesAdmin)
admin.site.register(StreamerServer)
admin.site.register(TvStreamerGroup)
admin.site.register(TvStream)




