#coding:utf-8
import urllib2
import time #for wait times
import re

print "\n-----------------------------------------"
#Get each page of movie ----In this version just do only one page
#init args
tag = 2011
page = 0
url = "http://movie.douban.com/tag/%d?start=%d&type=T"%(tag,page)

#movie_list [movie_name_1,movie_name_2,..]
#dictionary format
#movie_name:vaule
#vaule=movie_url,movie_rating,movie_review
print "Connect to douban_movie and get movie_info"
openurl = urllib2.urlopen(url)
content = openurl.read()
#获取页面数
tag_page = re.search('\d*</a>\s*<span class="next',content).group(0)
tag_page = int(re.search('\d*',tag_page).group(0))
for i in range(0,tag_page+1):
    time.sleep(2)
    tag = 2011
    page += 20
    url = "http://movie.douban.com/tag/%d?start=%d&type=T"%(tag,page)
    openurl = urllib2.urlopen(url)
    content = openurl.read()
    #得到只有movie的table的content
    tag_1 = content.find('<div class="">')
    tag_2 = content.find('<div class="paginator">')
    content = content[(tag_1+len('<div class="")')):tag_2]
    #looking for movie by regex
    #错了，因该根据电影名，然后来划出那部电影的范围，然后获取各值，然后才是赋值，不是获取全部，然后一个个去变列表再赋值
    movie_dic = {}
    vaule = []
    movie_list = []
    #开始抓取
    temp_movie = re.findall('<table[\s\S]*?table>',content)
    print "Get the page of %d movie list"%i
    print "This is start=%d content"%page
    for i in temp_movie:
        vaule = []
        #获取电影url
        temp_url = (re.search('<a href=".*?"',i)).group(0)[len('<a href="'):-1]
        vaule.append(temp_url)
        #获取电影评分
        temp_rating = (re.search('rating_nums">.*?<',i))
        if temp_rating:
            temp_rating = temp_rating.group(0)
            temp_rating = re.search('\d+',temp_rating)
            if temp_rating:
                temp_rating = temp_rating.group(0)
            else:
                temp_rating = 0
        else:
            temp_rating = 0
        temp_rating = float(temp_rating)
        vaule.append(temp_rating)
        #获取电影评论数
        temp_review = (re.search('<span class="pl".*\d',i))
        if temp_review:
            temp_review = temp_review.group(0)
            temp_review = re.search('\d+',temp_review).group(0)
        else:
            temp_review = 0
        temp_review = int(temp_review)
        vaule.append(temp_review)
        #获取电影名
        temp_name = (re.search('title=".*?"',i)).group(0)[len('title="'):-1]
        movie_dic[temp_name] = vaule
        movie_list.append(temp_name)
        print temp_name,movie_dic[temp_name]

#开始排序
#movie_dic[name][2]---movie rating
#movie_list
for i in range(len(movie_list)-1,0,-1):
    for j in range(0,i):
        if movie_dic[movie_list[j]][2] < movie_dic[movie_list[j+1]][2]:
            movie_list[j],movie_list[j+1] = movie_list[j+1],movie_list[j]

#保存文件
document  = file('Douban_movie','w')
#movie_dic format 
#[0]url [1]rating [2]review
#file format
#name rating review url
# i   movie_dic[i][1] movie_dic[i][2] movie_dic[i][0]
for i in movie_list:
    movie_info = "%s %.1f %d %s\n"%(i,movie_dic[i][1],movie_dic[i][2],movie_dic[i][0])
    document.write(movie_info)
