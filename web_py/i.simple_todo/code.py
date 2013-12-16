#!/usr/bin/env python
#coding:utf-8
import web
from config.url import urls
#可以看作config的url包，url包的urls类
#from i_config import url 这样写下边的urls就是url.urls

app = web.application(urls,globals())

if __name__ == "__main__":
    app.run()
