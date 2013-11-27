#coding:utf-8
import urllib2
import time #for wait times
import re

print "-----------------------------------------"
#Get each page of movie ----In this version just do only one page
#init args
page = 0
url = "http://movie.douban.com/tag/2011?start=%d&type=T"%(page)
document = ""#用来存储最后结果

def get_movie_list(url):
    #movie_list [movie_name_1,movie_name_2,..]
    #dictionary format
    #movie_name:vaule
    #vaule=movie_url,movie_rating,movie_review
    openurl = urllib2.urlopen(url)
    content = openurl.read()
    tag_1 = content.find('<div class="">')
    tag_2 = content.find('<div class="paginator">')
    content = content[(tag_1+len('<div class="")')):tag_2]
    print "Get content from HTML"
    #looking for movie by regex 错了，因该根据电影名，然后来划出那部电影的范围，然后获取各值，然后才是赋值，不是获取全部，然后一个个去变列表再赋值
    movie_dic = {}
    vaule = []
    movie_list = []
    
    #开始抓取
    temp_movie = re.findall('<table[\s\S]*?table>',content)
    print "Split movie from content"
    for i in temp_movie:
        vaule = []
        #获取电影url
        temp_url = (re.search('<a href=".*?"',i)).group(0)[len('<a href="'):-1]
        vaule.append(temp_url)
        #获取电影评分
        temp_rating = (re.search('rating_nums">.*?<',i)).group(0)[len('rating_nums">'):-1]
        temp_rating = float(temp_rating)
        vaule.append(temp_rating)
        #获取电影评论数
        temp_review = (re.search('<span class="pl".*\d',i)).group(0)[len('<span class="pl">)'):]
        temp_review = int(temp_review)
        vaule.append(temp_review)
        #获取电影名
        temp_name = (re.search('title=".*?"',i)).group(0)[len('title="'):-1]
        movie_dic[temp_name] = vaule
        movie_list.append(temp_name)
    return movie_dic

#开始排序
#movie_dic[name][2]
#movie_lsit
for i in range(len(movie_list)-1,0,-1):
    for j in range(0,i):
        if movie_dic[movie_list[j]][2] < movie_dic[movie_list[j+1]][2]:
            movie_list[j],movie_list[j+1] = movie_list[j+1],movie_list[j]
