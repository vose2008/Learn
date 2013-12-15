#!/usr/bin/env python
#coding:utf-8
import web

render = web.template.render('templates/')

web.template.Template.globals['render'] = render 
