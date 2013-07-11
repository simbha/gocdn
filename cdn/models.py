#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model
from django.db.models.aggregates import Sum
from datetime import datetime
from django.utils.encoding import smart_str
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext as _
from gocdn import settings
from gocdn.library.utilities import *
from gocdn.members.models import *



class CdnTypes(models.Model):
    name = models.CharField(verbose_name=u'CDN Tipleri', max_length='255')
    order = models.IntegerField(verbose_name=u'Sıra', default=None, null=True, blank=True)

    def __unicode__(self):
        return (u'%s')%self.name

    class Meta:
        verbose_name=u"CDN Tipi"
        verbose_name_plural = u"CDN Tipleri"


'''class CdnUrl(models.Model):
    url = models.URLField(verbose_name=u'CDN Linki')
    order = models.IntegerField(verbose_name=u'Sıra', default=None, null=True, blank=True)

    class Meta:
        verbose_name=u"CDN Linki"
        verbose_name_plural = u"CDN Linkleri"'''






class PushServers(models.Model):
    name = models.CharField(verbose_name=u'Push Server', max_length='255')
    order = models.IntegerField(verbose_name=u'Sıra', default=None, null=True, blank=True)

    def __unicode__(self):
        return (u'%s')%self.name

    class Meta:
        verbose_name=u"Push Server"
        verbose_name_plural = u"Push Server"



class PushZones(models.Model):
    name = models.CharField(verbose_name=u'Push Zone', max_length='255')
    server = models.ForeignKey(PushServers, verbose_name=u'Push Server', related_name='push_server', default=None, null=True, blank=True)
    user = models.ForeignKey(GoUser, related_name='push_user', verbose_name=u'Kullanıcı', default=None, null=True, blank=True)
    order = models.IntegerField(verbose_name=u'Sıra', default=None, null=True, blank=True)

    def __unicode__(self):
        return (u'%s')%self.name

    class Meta:
        verbose_name=u"Push Zone"
        verbose_name_plural = u"Push Zone"


class CacheExpiry(models.Model):
    name = models.CharField(verbose_name=u'Cache Expiry', max_length='255')
    order = models.IntegerField(verbose_name=u'Sıra', default=None, null=True, blank=True)

    def __unicode__(self):
        return (u'%s')%self.name

    class Meta:
        verbose_name=u"Cache Expiry"
        verbose_name_plural = u"Cache Expiry"


class UrlSigning(models.Model):
    name = models.CharField(verbose_name=u'Url Signing', max_length='255')
    order = models.IntegerField(verbose_name=u'Sıra', default=None, null=True, blank=True)

    def __unicode__(self):
        return (u'%s')%self.name

    class Meta:
        verbose_name=u"Url Signing"
        verbose_name_plural = u"Url Signing"


class Cdn(models.Model):
    is_push = models.BooleanField(verbose_name=u'PushZone Kullanılsın mı?', default=True)
    cdn_users = models.ForeignKey(GoUser, related_name='cdn_user', verbose_name=u'CDN Kullanıcısı')
    cdn_types = models.ForeignKey(CdnTypes,verbose_name=u'CDN Tipleri', related_name='cdn_types', null=True, blank=True)
    cdn = models.URLField(verbose_name=u'CNAME', default=None, null=True, blank=True, help_text=u'Örnek : isim.siteadi.com')
    #cdn_urls = models.URLField(verbose_name=u'CNAME', default=None, help_text=u'Örnek: cdn.siteniz.com (http:// or https:// olmadan)', null=True, blank=True)
    push_zone = models.ForeignKey(PushZones,verbose_name=u'Push Zone', related_name='cdn_push', null=True, blank=True)
    static_url = models.URLField(verbose_name=u'Orijinal web site', default=None, null=True, blank=True,help_text=u'Örnek: cdn.siteniz.com (http:// or https:// olmadan)',)
    #original_url = models.URLField(verbose_name=u'Orijinal web site', default=None, null=True, blank=True,help_text=u'Örnek: cdn.siteniz.com (http:// or https:// olmadan)',)
    cache_expiry = models.ForeignKey(CacheExpiry, related_name='cdn_cache', verbose_name='Cache Expiry', default=None, null=True, blank=True)
    url_signing = models.ForeignKey(UrlSigning, related_name='cdn_signing', verbose_name='Url Signing', default=0, null=True, blank=True)
    order = models.IntegerField(verbose_name=u'Sıra', default=None, null=True, blank=True)


    class Meta:
        verbose_name=u"CDN"
        verbose_name_plural = u"CDN"




