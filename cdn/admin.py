#encoding: utf-8
__author__ = 'jasmine'
from django.contrib import admin
from gocdn.members.models import *
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _
from gocdn.cdn.models import *


class CdnAdmin(admin.ModelAdmin):

    list_display = ['cdn_users','cdn_types','static_url']
    ordering = ['-id']
    search_fields = ['cdn_users','cdn_types','static_url']
    list_filter = ['cdn_users','cdn_types','static_url']
    list_editable = ['cdn_types','static_url']
    raw_id_fields = ['cdn_users']


admin.site.register(CdnTypes)
admin.site.register(Cdn,CdnAdmin)
admin.site.register(PushZones)
admin.site.register(PushServers)
admin.site.register(CacheExpiry)
admin.site.register(UrlSigning)

