#!/usr/bin/env python
#coding:utf-8

import datetime
from django.http import HttpResponse, Http404

def hello(request):
    #assert False
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"%now
    return HttpResponse(html)

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></hlml>"%(offset,dt)
    return HttpResponse(html)
