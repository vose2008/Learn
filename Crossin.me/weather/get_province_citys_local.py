#coding:utf-8
import urllib2

#Format content
def format_content(content):
    content = content.replace('{','')
    content = content.replace('}','')
    content = content.replace('"','')
    content = content.replace(',','\n')
    content = content.replace(':',' ')
    return content
#Write to file
def save_file(content):
    document = file('data','w')
    document.write(content)
    document.close()
#Get_number
def get_number(content):
    for i in range(len(content)):
        nu = content[i].index(' ')
        tmp = content[i]
        content[i]=tmp[0:nu]
    return content

#Get_province_info
url = 'http://www.weather.com.cn/data/city3jdata/china.html'
print 'Get\t'+url
open_url = urllib2.urlopen(url)
content = open_url.read()
content = format_content(content).split('\n')
content = get_number(content)
print "over"

#Get_city_info
total = ''
for i in content:
    url = "http://www.weather.com.cn/data/city3jdata/provshi/"+i+".html"
    print 'Get'+'\t'+url
    open_url = urllib2.urlopen(url)
    city_nu = open_url.read()
    city_nu = get_number(format_content(city_nu).split('\n'))
    for a in city_nu:
        city_code = i+a+'\n'
        total += city_code
city_nu = total.split('\n')
city_nu.pop(-1)
print "over"

#Get_local_info
total = ''
for i in city_nu:
    url = "http://www.weather.com.cn/data/city3jdata/station/"+i+".html"
    print 'Get'+'\t'+url
    open_url = urllib2.urlopen(url)
    local_nu = open_url.read()
    local_nu = format_content(local_nu).split('\n')
    for a in local_nu:
        local_info = i+a+'\n'
        total += local_info
print "over"
#save to file
save_file(total)
