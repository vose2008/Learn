#!usr/bin/env python
#coding:utf-8

from views import *
from django.conf.urls import patterns,url

urlpatterns = patterns('',
    url('^tags$',tags),
)
