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
from helpdesk.forms import *
from django.contrib import messages
from gocdn.members.models import GoUser



def help_desk(request):

    user = request.user
    #user = GoUser.objects.get(pk=request.user.id)
    print 'request.user',user
    if request.method == 'POST':
        form = HelpForm(request.POST)
        if form.is_valid():
            help = form.save(commit=False)
            help.help_user = user
            help.save()
            help.help_email()
            messages.add_message(request, messages.SUCCESS, 'Destek Mesajınız Başarı ile iletilmiştir.')
            return HttpResponseRedirect(reverse('help_list'))
    else:
        form = HelpForm()

    return render_to_response('helpdesk/help.html', {'form':form}, context_instance=RequestContext(request))


def help_list(request):
    list = Help.objects.filter(help_user=request.user)
    return render_to_response('helpdesk/helplist.html', {'list':list}, context_instance=RequestContext(request))



