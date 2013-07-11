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

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label="E-Posta Adresi",
        widget=forms.TextInput(attrs={'size':'50', 'class': 'input'}))
    password = forms.CharField(min_length=6,
        max_length=20,
        label="Parola",
        help_text="En az 6 karakterden oluşmalıdır.",
        widget=forms.PasswordInput(attrs={'size':8, 'class': 'input'}))
    passwordrep = forms.CharField(min_length=6,
        max_length=20,
        label="Parola (Tekrar)",
        widget=forms.PasswordInput(attrs={'size':8, 'class': 'input', 'equalTo': 'id_password'}))

    class Meta:
        model = GoUser
        fields = ['email','first_name','last_name','password','passwordrep']
        widgets={
            'email': forms.TextInput(attrs={'class': 'input'}),
            'first_name': forms.TextInput(attrs={'class': 'input'}),
            'last_name': forms.TextInput(attrs={'class': 'input'}),
            }

    def clean_email(self):
        e = self.cleaned_data['email']
        user = GoUser.objects.filter(email=e).count()
        if user == 0:
            return e
        else:
            raise forms.ValidationError("Bu e-posta adresi ile daha önce kayıt yapılmış!")

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 6:
            raise forms.ValidationError("Şifre en az 6 karakterli olmalıdır")
        else:
            return data

    def clean_passwordrep(self):
        passwordrep = self.cleaned_data['passwordrep']
        password = self.clean_password()
        if passwordrep != password:
            raise forms.ValidationError("Şifre ile aynı olmalıdır")
        else:
            return passwordrep



class MemberEdit(forms.ModelForm):

    class Meta:
        model = GoUser
        fields = ['tc_identity','mobile', 'email']


class ChangePasswordForm(PasswordChangeForm):

    new_password1 = forms.CharField(label=_("New password"), widget=forms.PasswordInput)



    def clean_new_password1(self):
        try:
            password1 = self.cleaned_data.get('new_password1')
            if not password1 or len(password1) < 6:
                raise forms.ValidationError("Şifre en az 6 karakterli olmalıdır")
            else:
                return password1
        except:
            settings.process_exception()
            raise forms.ValidationError("Şifre en az 6 karakterli olmalıdır")