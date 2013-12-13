#coding:utf-8
import urllib2
import json
from city import city

cityname = raw_input('City Name Please:')
city_nu = city.get(cityname)
if city_nu:
    url = 'http://www.weather.com.cn/data/cityinfo/'+city_nu+'.html'
    web = urllib2.urlopen(url)
    data = json.loads(web.read())
    # weather to read
    info = data['weatherinfo']
    print ' %s To day\n %s %s ~ %s'%(info['city'],info['weather'],info['temp1'],info['temp2']) 
else:
    print '404 city not found'
