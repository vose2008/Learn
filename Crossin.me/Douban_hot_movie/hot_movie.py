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
print "Get content from HTML"
#looking for movie by regex 错了，因该根据电影名，然后来划出那部电影的范围，然后获取各值，然后才是赋值，不是获取全部，然后一个个去变列表再赋值
movie_dic = {}
vaule = []
#
temp_movie = re.findall('<table[\s\S]*?table>',content)
print "Split movie from content"
for i in temp_movie:
    vaule = []
    temp_url = (re.search('<a href=".*?"',i)).group(0)[len('<a href="'):-1]
    vaule.append(temp_url)
    print temp_url
    temp_rating = (re.search('rating_nums">.*?<',i)).group(0)[len('rating_nums">'):-1]
    float(temp_rating)
    vaule.append(temp_rating)
    print temp_rating
    temp_review = (re.search('<span class="pl".*?\)',i)).group(0)[len('<span class="pl">\)'):-4]
    vaule.append(temp_review)
    print temp_review
    break
    temp_name = (re.search('title=".*?"',i)).group(0)[len('title="'):-1]
    movie_dic[temp_name]=value
