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
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage,send_mail
from django.template.loader import render_to_string
from gocdn.members.models import *


class HelpSubject(models.Model):
    subject = models.CharField(verbose_name=u'Kou', max_length=255)
    order = models.IntegerField(verbose_name=u'Sıra')

    def __unicode__(self):
        return self.subject


    class Meta:
        verbose_name = u'Destek Kategorisi'
        verbose_name_plural = u'Destek Kategorileri'

    def help_subject(self):
        return self.subject

class Help(models.Model):
    help_title = models.CharField(verbose_name='Başlık', max_length=255)
    help_subject = models.ForeignKey(HelpSubject, verbose_name=u'Yardım Konusu')
    help_content = models.TextField(verbose_name=u'Mesaj')
    help_user = models.ForeignKey(GoUser, verbose_name=u'Kullanıcı')



    def __unicode__(self):
        return self.help_title



    class Meta:
        verbose_name = u'Destek Mesajı'
        verbose_name_plural = u'Destek Mesajları'



    def help_email(self):

        subject = self.help_title

        html_content = render_to_string('email/help_mail.html',
                {'email': settings.HELP_MAIL, 'subject':subject, 'title':self.help_subject, 'content':self.help_content})
        msg = EmailMessage(subject, self.help_content, settings.DEFAULT_FROM_EMAIL, [settings.HELP_MAIL])
        msg.content_subtype = "html"
        msg.send()


