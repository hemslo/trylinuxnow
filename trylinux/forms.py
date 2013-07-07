# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.Form):
    username = forms.CharField(label=_(u"username"),
                               max_length=30,
                               widget=forms.TextInput(attrs={'size': 20}))
    password = forms.CharField(label=_(u"password"),
                               max_length=30,
                               widget=forms.PasswordInput(attrs={'size': 20}))

    def clean_username(self):
        '''Verify duplicate username'''
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(_(u"duplicate username"))



class LoginForm(forms.Form):
    username = forms.CharField(label=_(u"username"),
                               max_length=30,
                               widget=forms.TextInput(attrs={'size': 20}))
    password = forms.CharField(label=_(u"password"),
                               max_length=30,
                               widget=forms.PasswordInput(attrs={'size': 20}))
