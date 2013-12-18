#!/usr/bin/env python
#coding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin

from mysite.views import * 

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$',hello),
    url('^hello/$',hello),
    url('^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
)
