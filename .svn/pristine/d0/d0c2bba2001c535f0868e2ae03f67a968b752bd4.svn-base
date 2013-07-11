#encoding: utf-8

from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext


def index(request):
    #menu = Menu.objects.all().order_by('menu_order')
    return render_to_response('index.html',
            #{'menu':menu},
        context_instance=RequestContext(request))