# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.utils.translation import ugettext_lazy as _
from forms import RegisterForm, LoginForm


def index(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
    else:
        user = ''
    registerform = RegisterForm()
    loginform = LoginForm()
    return render_to_response(
        'index.html',
        {'registerform': registerform, 'loginform':loginform, 'user':user},
        context_instance=RequestContext(request)
    )


def register(request):
    '''register'''
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username, '', password)
            user.save()
            _login(request, username, password)
    return HttpResponseRedirect('/')


def login(request):
    '''login'''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request, form.cleaned_data["username"], form.cleaned_data["password"])
    return HttpResponseRedirect('/')


def _login(request, username, password):
    '''login core'''
    ret = False
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            auth_login(request, user)
            ret = True
    else:
        messages.add_message(request, messages.INFO, _(u'user not exist'))
    return ret


def logout(request):
    '''logout'''
    auth_logout(request)
    return HttpResponseRedirect('/')
