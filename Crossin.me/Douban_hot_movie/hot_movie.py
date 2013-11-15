#coding:utf-8
import urllib2
import time #for wait times


#Get each page movie in this version just do only one page
#init args
page = 0
url = "http://movie.douban.com/tag/2011?start=%d&type=T"%(page)
document = ""
movie_list = []

openurl = urllib2.urlopen(url)
content = openurl.read()
tag_1 = content.find('<div class="">')
tag_2 = content.find('<div class="paginator">')
content = content[(tag_1+len('<div class="")')):tag_2]
print content

