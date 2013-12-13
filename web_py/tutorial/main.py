#coding:utf-8
import  web

render = web.template.render('templates/')#获得模板路径
urls = ('/', 'index')
#urls = ('/(.*)', 'index')
#这个正则我理解为/主页面后一个单词(参数)

class index:
    def GET(self):
        #name = "Bob"
        i = web.input(name=None)#i.name默认值为None
        return render.index(i.name)
    #def GET(self,name):
    #    return render.index(name)
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
