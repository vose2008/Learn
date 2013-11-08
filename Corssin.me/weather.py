#coding:utf-8
import urllib2
import json

city_nu = raw_input("Enter city name:")
url = 'http://www.weather.com.cn/data/cityinfo/'+city_nu+'.html'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read()
print content
