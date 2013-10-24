[1].[代码] [Python]代码 跳至 [1]
view sourceprint?
1
import urllib2
2
import cookielib
3
import urllib
4
cookie = cookielib.CookieJar()
5
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
6
response = opener.open('http://t.sohu.com/settings/bindMobile/registSendVerificationCode')
7
data={'mobileNumber':'13558233012'}
8
r=opener.open('http://t.sohu.com/settings/bindMobile/registSendVerificationCode',urllib.urlencode(data))
9
print r.read()