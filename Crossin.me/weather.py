#coding:utf-8
import urllib2
import json
from city import city

cityname = raw_input('city name please')
city_nu = city.get(cityname)
if city_nu:
    url = 'www.weather.com/cn/data/cityinfo/'+city_nu+'.html'
    web = urllib2.urlopen(url)
    content = web.read()
    print content
