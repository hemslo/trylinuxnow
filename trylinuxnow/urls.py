#-*-coding:utf8-*-
from django.conf.urls import patterns, url, include
from trylinux.views import index, register, login, logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', index),
                       url(r'^register/$', register),
                       url(r'^login/$', login),
                       url(r'^logout/$', logout),
                       # Uncomment the next line to enable the admin:
                       url(r'^teach/', include(admin.site.urls)),
                       #url(r'^postcommand/$', postcommand),
                       #url(r'^learn/$', learn),
                       #url(r'^courses/(\d+)/stages/(\d+)', courses),
                       #url(r'^create/$',create),
                       )
