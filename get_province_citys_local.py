#coding:utf-8
import urllib2
import json

#Get_province_info
url = 'http://www.weather.com.cn/data/city3jdata/china.html'
open_url = urllib2.urlopen(url)
content = open_url.read()
content = str(content)
#Format content
content = content.replace('{','')
content = content.replace('}','')
content = content.replace('"','')
content = content.replace(',','\n')
#Write to file
document = file('data','w')
document.write(content)
document.close()
#Get province number
document = file('data')
content = document.readlines()
for i in range(len(content)):
    nu = content[i].index(':')
    tmp = content[i]
    content[i]=tmp[0:nu]
#Get_city_info
nu = ###############
url = 'http://www.weather.com.cn/data/city3jdata/provshi/'+nu+'.html'
