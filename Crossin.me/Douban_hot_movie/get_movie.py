import urllib2

#get all page of 2011

page = 0
url = "http://movie.douban.com/tag/2011?start=%d&type=T"%(page)
document = ''
while page < 1401:
    openurl = urllib2.urlopen(url)
    content = openurl.read()
    document += content
    page += 20

f = file('movie','w')
f.write(document)
f.close
