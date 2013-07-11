# encoding: utf-8
from local_settings import *
import os
import sys

SEND_BROKEN_LINK_EMAILS = False
SERVER_EMAIL = ''


TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'tr_TR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True




PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
SECRET_KEY = '3ogg13kxs2h(!dz0-qqh9y8u2idmjz@)1kgb8&xi@@!h1td@vg'
#STATIC_URL = '/static/'
MEDIA_URL = '/static/'

HELP_MAIL = 'help@gostream.com'

EXCHANGES = ((0, "TL"),
             (1, "USD"),
             (2, "EUR"))

ADDRESS_TYPE = (
    (1, "Fatura Adresi"),
    (2, "Teslimat Adresi")
    )

PRODUCT_PER_PAGE = 16

PAYMENT_TYPES = (
    (1, u'Kredi kartı ile ödeme'),
    #(2, u'Paypal ile ödeme')
    #(3, u'Banka havalesi ile ödeme')
    )
BANK_TRANSFER_DISCOUNT_PERCENT = 0 #havale indirimi
CC_CARD_TYPES = (
    (1, 'Visa'),
    (2, 'MasterCard'),
    (3, 'American Express')
    )

'''STATICFILES_DIRS = ()


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    )'''

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    #"modules.context_processors.active_tab",
    'django.contrib.messages.context_processors.messages',
    )


TEMPLATE_LOADERS = (
    #('django.template.loaders.cached.Loader', (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader',
    'django.template.loaders.app_directories.Loader',
    )


MIDDLEWARE_CLASSES = (
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'breadcrumbs.middleware.BreadcrumbsMiddleware',

    )

ROOT_URLCONF = 'gocdn.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'south',
    'cdn',
    'tvstream',
    'members',
    'helpdesk',
    'faq',
    'home',
    'product'




    #'sitetree'
    )

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    )

INTERNAL_IPS = ('127.0.0.1',)


AUTHENTICATION_BACKENDS = (
    'gocdn.members.models.GoUserModelBackend',
    )

CUSTOM_USER_MODEL = 'members.GoUser'


LOGIN_REDIRECT_URL = "/cdn/"
LOGIN_URL = "/"
LOGOUT_URL = "/member/logout/"

TINYMCE_FILEBROWSER = False
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace,fullpage,preview,fullscreen,table,contextmenu",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'nowrap': True,
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_buttons1': "preview,fullscreen,code,separator,copy,paste,cut,separator,undo,redo,separator,hr,removeformat,visualaid,separator,sub,sup,separator,charmap",
    'theme_advanced_buttons2': "forecolor,backcolor,fontselect,fontsizeselect,separator,bold,italic,underline,strikethrough,justifyleft,justifycenter,justifyright,justifyfull,bullist,numlist,separator,outdent,indent",
    'theme_advanced_buttons3': "tablecontrols,table,row_props,cell_props,delete_col,delete_row,col_after,col_before,row_after,row_before,split_cells,merge_cells",
    }

DATETIME_INPUT_FORMATS = ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d')
DATE_INPUT_FORMATS = ('%Y-%m-%d')
USE_THOUSAND_SEPARATOR = True
THOUSAND_SEPARATOR = '.'



CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots',)
CAPTCHA_FILTER_FUNCTIONS = ''


SENTRY_TESTING = True
def process_exception():
    import sys, traceback
    (exc_type, exc_info, tb) = sys.exc_info()
    response = "%s\n" % exc_type.__name__
    response += "%s\n\n" % exc_info
    response += "TRACEBACK:\n"
    for tb in traceback.format_tb(tb):
        response += "%s\n" % tb
        #logging.debug(response)
    print response

