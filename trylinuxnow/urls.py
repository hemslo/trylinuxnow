#-*-coding:utf8-*-
from django.conf.urls import patterns, url, include
from trylinux.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^register/$', register),
                       url(r'^login/$', login),
                       url(r'^logout/$', logout),
)
