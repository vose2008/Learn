#coding:utf-8
import urllib2
import time #for wait times
import re


#Get each page of movie ----In this version just do only one page
#init args
page = 0
url = "http://movie.douban.com/tag/2011?start=%d&type=T"%(page)
document = ""
#list [movie_name,..]
#dictionary movie_name:vaule vaule=movie_url,movie_rating,movie_review

openurl = urllib2.urlopen(url)
content = openurl.read()
tag_1 = content.find('<div class="">')
tag_2 = content.find('<div class="paginator">')
content = content[(tag_1+len('<div class="")')):tag_2]
print content
#looking for movie by regex 错了，因该根据电影名，然后来划出那部电影的范围，然后获取各值，然后才是赋值，不是获取全部，然后一个个去变列表再赋值
temp_name = re.findall('title=".*"',content)
for i in temp_name:
    name=i[len('title="'):-1]
    name={}
temp_url = re.findall('<a href=".*"',content)
for i in temp_url:
    name=i[len('<a href="'):-1]
    global vaule=[name] 
temp_rating = re.findall('rating_nums">.*<',content)
    float(name)=i[len('rating_nums">'):-1]
    vaule.append(name)
temp_review = re.findall('<span class="pl".*<',content)
for i in vaule:
    print i
