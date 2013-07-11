__author__ = 'yasemenkarakoc'
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
from library.thumbs import *

class Positions(models.Model):
    position = models.CharField(verbose_name=u'Konum', max_length=255)
    order = models.IntegerField(verbose_name=u'Sıra')

    def __unicode__(self):
        return self.position

    class Meta:
        verbose_name = u'Konum'
        verbose_name_plural = u'Konum'


class MainPage(models.Model):
    title = models.CharField(verbose_name=u'Baslik', max_length=400)
    slug = models.SlugField(verbose_name=u'Link')
    position = models.ForeignKey(Positions, verbose_name=u'Konum', default=None, null=True, blank=True)
    abstract = models.TextField(verbose_name=u'Hülasa', help_text=u'Anasayfada Gözüken kısa metin', default=None, null=True, blank=True)
    content = models.TextField(verbose_name=u'Icerik')
    photo = models.ImageField(verbose_name=u'Imaj',upload_to='dynamic/userimages', default=None, null=True, blank=True)
    status = models.BooleanField(verbose_name=u'Durum', default=True)
    add_date = models.DateTimeField(verbose_name=u'Ekleme Zamani', auto_now_add=True, default=None, null=True, blank=True)
    order = models.IntegerField(verbose_name=u'Sıra')
    top_menu = models.BooleanField(verbose_name=u"Üst menü'de gösterilsin mi?", default=False, help_text=u'Üst menüde linki gösterilecekse işaretlensin')
    middle_menu = models.BooleanField(verbose_name=u"Orta menü'de gösterilsin mi?", default=False, help_text=u'Orta menüde linki gösterilecekse işaretlensin')
    footer_menu = models.BooleanField(verbose_name=u"Alt menü'de gösterilsin mi?", default=False, help_text=u'Alt menüde linki gösterilecekse işaretlensin')
    is_slogan = models.BooleanField(verbose_name=u'Slogan da gösterilsin mi?', default=False, help_text=u'Sloganda gösterilecekse işaretlensin')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'İçerik'
        verbose_name_plural = u'İçerik'



class Customers(models.Model):
    title = models.CharField(verbose_name=u'Baslik', max_length=400)
    link = models.CharField(verbose_name=u'Link', max_length=400)
    photo = models.ImageField(verbose_name=u'Imaj',upload_to='dynamic/userimages/refs', default=None, null=True, blank=True)


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Referans'
        verbose_name_plural = u'Referanslar'
