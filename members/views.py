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



def gostream_register(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    if request.method == 'POST' and 'submit' in request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 1
            user.is_active = False
            #user.username = hashlib.md5(user.email + str(datetime.now())).hexdigest()[:30]
            user.username = form.cleaned_data['email']
            user.activation_code = create_activation_code(10)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user.sendActivationMail()
            print user.__dict__
            return render_to_response('firstapps/initial_registration_success.html', {'user' : user} , context_instance=RequestContext(request))

    else:
        form = RegisterForm()




    return render_to_response('register.html', {'form':form}, context_instance=RequestContext(request))

def user_activate(request, actcode):
    user = get_object_or_404(GoUser, activation_code = actcode, is_active = False)
    user.is_active = True
    user.activation_code = '!'
    user.save()
    lastname = user.last_name
    return render_to_response('member/activation_success.html', locals(), context_instance=RequestContext(request))



def gostream_login(request):

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print user
        if user is not None:
            if user.is_active:
                login(request, user)
                # success
                if request.POST['next']:
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('member_area'))
            else:
                # disabled account
                return direct_to_template(request, 'member/inactive_account.html')
        else:
            # invalid login
            return direct_to_template(request, 'member/invalid_login.html')

    return render_to_response('member/login_required.html',
            {

        },
        context_instance=RequestContext(request))




def gostream_logout(request):
    logout(request)
    return direct_to_template(request, 'member/login_required.html')


def first_screen(request):
    if request.user.is_authenticated():
        print 'its ok'
        return HttpResponseRedirect(reverse('member_area'))
    else:
        return HttpResponseRedirect(reverse('gostream_login'))

@login_required
def member_area(request):
    user = request.user
    return render_to_response('index.html',
            {
                'user':user
            },
        context_instance=RequestContext(request))


@login_required
def create_cdn(request):
    user = GoUser.objects.get(pk=request.user)
    if request.method == "POST" and 'cdnsubmit' in request.POST:
        form = CdnCreateForm(request.POST)
        if form.is_valid():
            cdn = form.save(commit=False)
            cdn.cdn_users = user
            cdn.save()
            return HttpResponseRedirect(reverse('cdn_list'))
    else:
        form = CdnCreateForm()



    return render_to_response('member/create_cdn.html', {
        'form': form,
        },context_instance=RequestContext(request))


@login_required
def cdn_list(request):

    cdn_list = Cdn.objects.filter(cdn_users=request.user)

    return render_to_response('member/cdn_list.html', {
        'cdn_list':cdn_list
        },context_instance=RequestContext(request))


@login_required
def cdn_edit(request,id):

    cdn = get_object_or_404(Cdn, pk=id)
    form = CdnCreateForm(instance=cdn)
    if request.method == 'POST':
        form = CdnCreateForm(request.POST,instance=cdn)
        if form.is_valid():
            c = form.save(commit=False)
            c.save()
            return HttpResponseRedirect(reverse('cdn_list'))

    return render_to_response('member/cdn_edit.html', {
        'id':id,
        'form':form
    },context_instance=RequestContext(request))


@login_required
def create_pushzone(request):
    user = GoUser.objects.get(pk=request.user)

    if request.method == 'POST':
        form = PushZoneCreateForm(request.POST)
        if form.is_valid():
            push = form.save(commit=False)
            push.user = user
            push.save()
            return HttpResponseRedirect(reverse('push_list'))
    else:
        form = PushZoneCreateForm()


    return render_to_response('member/create_pushzone.html', {
        'form':form
    },context_instance=RequestContext(request))


@login_required
def push_list(request):
    user = GoUser.objects.get(pk=request.user)
    push_list = PushZones.objects.filter(user= user)
    print push_list
    return render_to_response('member/push_list.html', {
        'push_list':push_list
    },context_instance=RequestContext(request))




@login_required
def push_edit(request,id):

    push = get_object_or_404(PushZones, pk=id)
    form = PushZoneCreateForm(instance=push)
    if request.method == 'POST':
        form = PushZoneCreateForm(request.POST,instance=push)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('push_list'))

    return render_to_response('member/push_edit.html', {
        'id':id,
        'form':form
    },context_instance=RequestContext(request))






@login_required
def account_edit(request):
    print request.user
    form = MemberEdit(instance=request.user)
    if request.method == 'POST':
        form = MemberEdit(request.POST, instance=request.user)

        if form.is_valid():
            u = form.save(commit=True)
            u.mobile = request.POST['mobile']
            u.save()
            print 'user', u
            return HttpResponseRedirect(reverse('member_area'))

    return render_to_response('member/account_edit.html', {
        'form':form,
    },context_instance=RequestContext(request))


