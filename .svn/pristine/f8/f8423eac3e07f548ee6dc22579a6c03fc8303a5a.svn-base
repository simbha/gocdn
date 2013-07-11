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



class Faqs(models.Model):
    HEADER = 2
    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE, _('Aktif')),
        (INACTIVE, _('Pasif')),
        )
    question  = models.TextField(_(u'soru'), help_text=_(u'Soru'))
    answer = models.TextField(_(u'cevap'), blank=True, help_text=_(u'Cevap'))
    slug = models.SlugField(_(u'slug'), max_length=100)
    status = models.IntegerField(_(u'status'),choices=STATUS_CHOICES, default=INACTIVE)
    sort_order = models.IntegerField(_(u'sort order'), default=0)


    class Meta:
        verbose_name = _(u"Sıkça Sorulan Soru")
        verbose_name_plural = _(u"Sıkça Sorulan Sorular")
        ordering = ['sort_order']

    def __unicode__(self):
        return self.question

    def is_active(self):
        return self.status == Faqs.ACTIVE


