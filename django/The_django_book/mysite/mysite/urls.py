#!/usr/bin/env python
#coding:utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin

from mysite.views import * 
from books import views as books_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$',hello),
    url('^hello/$',mypage),
    url('^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^meta$',display_meta),
    #forms
    url(r'^search-form/$',books_views.search),
    url(r'^search/$',books_views.search)
)
