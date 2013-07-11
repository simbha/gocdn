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


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.main', name='home'),
    url(r'^panel/$', 'gocdn.members.views.first_screen', name='first_screen'),
    # url(r'^gostream/', include('gostream.foo.urls')),
    #url(r'^admin_tools/', include('admin_tools.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'gostream.streaming.views.upload', name='upload'),

    #register
    url( r'^register/', 'gocdn.members.views.gostream_register',name= 'gostream_register' ),
    url(r'^member/activate/(?P<actcode>\w+)/', 'gocdn.members.views.user_activate', name='user_activate'),
    url(r'^go/$', 'gocdn.members.views.gostream_register', name='gostream_register'),
    url(r'^login/$', 'gocdn.members.views.gostream_login',name='gostream_login'),
    url(r'^logout/$', 'gocdn.members.views.gostream_logout',name='gostream_logout'),
    url(r'^mygostream/$', 'gocdn.members.views.member_area',name='member_area'),

    #cdn islemleri
    url(r'^createcdn/$', 'gocdn.members.views.create_cdn',name='create_cdn'),
    url(r'^cdnlist/$', 'gocdn.members.views.cdn_list',name='cdn_list'),
    url(r'^cdnedit/(?P<id>\d+)/$', 'gocdn.members.views.cdn_edit', name="cdn_edit"),

    #pushzone islemleri

    url(r'^createpushzone/$', 'gocdn.members.views.create_pushzone',name='create_pushzone'),
    url(r'^pushedit/(?P<id>\d+)/$', 'gocdn.members.views.push_edit', name="push_edit"),
    url(r'^pushlist/$', 'gocdn.members.views.push_list',name='push_list'),

    #kullanici islemleri
    url(r'^account/$', 'gocdn.members.views.account_edit',name='account_edit'),

    #change pass
    url(r'^password/change/$', password_change , {
        'template_name': 'passwords/password_change.html',
        'password_change_form': ChangePasswordForm,
        'post_change_redirect' : '/password/change/done/'
    },name='password_change'),
    url(r'^password/change/done/$', password_change_done, {
        'template_name': 'passwords/password_change_done.html'
    }),
    #product
    #url(r'^pricing/$', include('gocdn.product.urls')),
    url(r'^pricing/$', 'gocdn.product.views.pricing', name='pricing'),



    url(r'^help/', include('gocdn.helpdesk.urls')),
    url(r'^sss/', include('gocdn.faq.urls')),


    #home

    url(
        r'^main/(?P<slug>[^\.]+)','home.views.main_view',name='main_view'),

)
if settings.DEBUG:
    # add one of these for every non-static root you want to serve
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # this take cares of static media (i.e. bundled in apps, and specified in settings)
    urlpatterns+= staticfiles_urlpatterns()


urlpatterns += patterns('',
    (r'^static/(?P<path>.*\.(?i)(css|js|jpg|png|gif|ico|swf|html|htm|doc|pdf|txt))$',
     'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*\.(?i)(css|js|jpg|png|gif|ico|swf|html|htm|doc|pdf|txt))$',
     'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^accounts/login/$', 'direct_to_template', {'template': 'member/login_required.html'}),
)

