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
#dictionary movie_name:movie_url,movie_rating,movie_review

openurl = urllib2.urlopen(url)
content = openurl.read()
tag_1 = content.find('<div class="">')
tag_2 = content.find('<div class="paginator">')
content = content[(tag_1+len('<div class="")')):tag_2]
print content
#looking for movie by regex
temp_name = re.findall('title=".*"',content)
for i in temp_name:
    name=i[len('title="'):-1]
    name={}
temp_url = re.findall('<a href=.* ',content)
temp_rating = re.findall('rating_nums.*<',content)
temp_review = re.findall('<span class="pl".*<',content)
