#encoding: utf-8
from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.utils.http import int_to_base36
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.forms.extras import SelectDateWidget
from django.contrib.localflavor.tr.forms import TRPhoneNumberField, TRProvinceSelect, TRIdentificationNumberField
from datetime import datetime, timedelta
from django.utils.http import int_to_base36
from django.utils.translation import ugettext_lazy as _
from django.core.validators import email_re
from django.utils.translation import ugettext as _
from django.forms.formsets import BaseFormSet
from django.forms.models import BaseModelFormSet, BaseFormSet
from django.core.validators import validate_email
from captcha.fields import CaptchaField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from gocdn.members.models import *
from gocdn.cdn.models import *

'''
cdn ctrate
'''
class CdnCreateForm(forms.ModelForm):
    class Meta:
        model = Cdn
        fields = ['is_push','push_zone','cdn_types','cdn','static_url','cache_expiry','url_signing']


class PushZoneCreateForm(forms.ModelForm):
    class Meta:
        model = PushZones
        fields = ['name', 'server']


