#!/usr/bin/env python
#coding:utf-8

import datetime
import MySQL
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render #if we do this no more needs HttpResponse get_template Context

def hello(request):
    #assert False
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>"%now
    #t = get_template('current_datetime.html')
    #c = Context({'current_date':now})
    #html = t.render(Context({'current_date':now}))
    #return HttpResponse(html)
    return render(request,'current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request,'hours_ahead.html',{'hour_offset':offset,'next_time':dt}) 

def mypage(request):
    now = datetime.datetime.now()
    return render(request,'mypage.html',{'current_date':now,'title':'TIME'})

def book_list(request):
    db = MySQL.connect(user='root',db='test',passwd='75811239',host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request,'book_list.html',{'names':names})
