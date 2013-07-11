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


class StreamerTypes(models.Model):
    type = models.CharField(verbose_name=u'yayıncı Grubu', max_length=255)
    type_order = models.IntegerField(verbose_name='Sıra')


    class Meta:
        verbose_name = u'yayıncı tipi'
        verbose_name_plural = u'yayıncı tipi'

class StreamerServer(models.Model):
    server_name = models.CharField(verbose_name=u'Sunucu ismi', max_length=255)
    server_url = models.CharField(verbose_name=u'Sunucu Linki', max_length=255)
    server_order = models.IntegerField(verbose_name='Sıra')


    class Meta:
        verbose_name = u'yayıncı tipi'
        verbose_name_plural = u'yayıncı tipi'


class TvStreamerGroup(models.Model):
    group = models.CharField(verbose_name=u'yayıncı Grubu', max_length=255)
    group_order = models.IntegerField(verbose_name='Sıra')


    class Meta:
        verbose_name = u'yayıncı Grubu'
        verbose_name_plural = u'yayıncı Grubu'

class TvStream(models.Model):
    name = models.CharField(verbose_name=u'isim', max_length=255)
    group = models.ForeignKey(TvStreamerGroup,verbose_name=u'yayıncı Grubu', related_name='streamer_group')
    description = models.TextField(verbose_name=u'Açıklama', max_length=255)
    logo = models.ImageField(verbose_name=u"Logo", upload_to="streamer/videos/", default=None,null=True, blank=True)
    email = models.EmailField(verbose_name=u'E-Posta')
    website = models.CharField(verbose_name=u'web site', max_length=255)
    type = models.ForeignKey(StreamerTypes, verbose_name=u'yayıncı tipi', related_name='streamer_type')
    server = models.ForeignKey(StreamerServer, verbose_name=u'Sunucu', related_name='streamer_server')
    create_date = models.DateTimeField(verbose_name=u'Oluşturma Tarihi', auto_now_add=True)
    stream_order = models.IntegerField(verbose_name=u'Sıra')
    picture = models.CharField(verbose_name='snapshot', max_length=255)


    class Meta:
        verbose_name = u'yayıncı'
        verbose_name_plural = u'yayıncı'

