import urllib2
import time #for wait times


#Get each page movie in this version just do only one page
page = 0
url = "http://movie.douban.com/tag/2011?start=%d&type=T"%(page)
document = ""

openurl = urllib2.urlopen(url)
content = openurl.read()
tag_1 = content.find('<div class="">')
tag_2 = content.find('<div class="paginator")')
content = contnet[tag_1+
