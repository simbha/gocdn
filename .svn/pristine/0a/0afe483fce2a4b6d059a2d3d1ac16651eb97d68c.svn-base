__author__ = 'yasemenkarakoc'
# encoding: utf-8
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from gocdn import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from gocdn.members.forms import *
from django.contrib.auth.views import password_reset, password_reset_complete, password_reset_done, password_reset_confirm,password_change,password_change_done

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('gocdn.helpdesk.views',

    url(r'^send/$', 'help_desk', name='help_desk'),
    url(r'^helplist/$', 'help_list', name='help_list'),
)
