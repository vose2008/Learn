###开始一个项目

一旦你安装好了python，Django和（可选的）数据库及其相关库与服务后，你就可以通过创建一个project（项目），迈出开发Django应用的第一步  

项目（project）是 Django 实例的一系列设置的集合，它包括数据库配置、Django特定选项以及应用程序的设置  

如果第一次使用Django，必须进行一些初始化设置工作。新建一个工作目录，例如 /home/username/djcode/ ，然后进入该目录。  

- - -
>这个目录该放哪儿？  

>如果有PHP编程的背景的话，你可能习惯将代码都放在 Web 服务器的文档根目录（例如 /var/www 这样的地方）。而在 Django 中，把任何python代码放到web server的根(root)目录与其它web文档混在一起都不是一个好主意，因为这样做有能使别人通过网络看到你的源代码的风险，那就太糟了。  

>所以，把代码放置到根目录 **之外** 的其它目录中。  
- - -

转到你创建的目录，运行命令django-admin.py startproject mysite。这样就会在你当前目录下创建一个目录。mysite  

- - -
>注意  
>如果用的是 setup.py 工具安装的 Django， django-admin.py 应该已经被加入了系统路径（环境变量中）  

>如果你使用的是开发者版本，你会在 djmaster/django/bin 下发现 django-admin.py。但因为以后你会经常用到django-admin.py，所以还是把它加入到你的系统路径中比较好。在Unix中，你可以创建一个链接到你的 /usr/local/bin 来达到这个目的，使用的命令可以像这个样子：
sudo ln -s /path/to/django/bin/django-admin.py /usr/local/bin/django-admin.py.
>在Windows中，你需要修改你的PATH环境变量。
>如果你的django是从Linux发行版中安装的，那么，django-admin.py常会被django-admin替代。
- - -

如果在运行 django-admin.py startproject 的时候，你看到"permission denied"（权限拒绝）的提示，你应当修改这个文件的权限。切换到你django-admin.py的所在目录（例子. cd/usr/local/bin），运行命令chmod +x django-admin.py 。

startproject 命令创建了，1个目录，其包含5个文件：
''''
mysite/  
    manage.py  
    mysite/  
    __init__.py  
    settings.py  
    urls.py  
    wsgi.py  
''''
