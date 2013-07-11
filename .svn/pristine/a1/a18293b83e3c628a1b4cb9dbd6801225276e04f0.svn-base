#encoding: utf-8
from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404, Http404, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_reset
from django.utils import simplejson
from captcha import *
import hashlib, datetime, time
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, get_backends
import gocdn.settings as settings
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from currencies.models import Currency
from gocdn.members.forms import *
from datetime import date,datetime
from gocdn.library.utilities import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from cdn.forms import *
from home.models import *

def main(request):
    customers = Customers.objects.all()
    #topmenu = MainPage.objects.filter(position=2, status=True).order_by('-order')
    slogan = MainPage.objects.filter(is_slogan=True, status=True).order_by('-id')[0]
    return render_to_response('home/home.html', {
        'slogan':slogan,
        'customers':customers
    }, context_instance=RequestContext(request))


def main_view(request,slug):
    query = get_object_or_404(MainPage,slug=slug, status=True)

    return render_to_response('home/view.html', {
        'query':query,

        }, context_instance=RequestContext(request))

