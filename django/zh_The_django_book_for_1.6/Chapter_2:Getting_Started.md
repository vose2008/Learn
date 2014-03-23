###开始一个项目

一旦你安装好了python，Django和（可选的）数据库及其相关库与服务后，你就可以通过创建一个project（项目），迈出开发Django应用的第一步。  

项目（project）是 Django 实例的一系列设置的集合，它包括数据库配置、Django特定选项以及应用程序的设置。  

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

>mysite/  
manage.py  
>>mysite/  
__init__.py  
settings.py  
urls.py  
wsgi.py   

- - -
>注释  
>与你看到的不一样？
>这是Django1.4及以上版本的默认布局。如果你看到一个单层次布局（内部没有mysite/ 子目录），那么你可能使用的是一个与本教程版本不同的Django版本。本书面对的是Django1.4及以上的版本。如果你使用的是旧版本，可以查询Django官方文档。
>Django1.X 版本文档可以在此找到：
>https://docs.djangoproject.com/en/1.X/

- - -

文件如下：  
+ mysite/：最外层的 mysite/ 文件夹只是项目的一个容器，名字无关紧要，你可以重命名为任何你想要的名字。
+ manage.py：一个命令行工具，允许你以多种方式通过它与你现在这个Django项目进行交互。键入python manage.py help 看看它能做什么。你不应当去编辑这个文件；在这个目录下生成它纯粹是出于方便。
+ mysite/mysite/：内层的 mysite/ 文件夹实际上是你项目的一个python包。它的这个名字是当你导入其中任何内容时要用到的名字（例如：import mysite.settings）。
+ __init__.py：让python把该目录当成一个开发包（即一组模块）所需的文件。这是一个空文件，一般你不需要修改它。
+ settings.py：该Django项目的设置或配置。你应该查看并理解这个文件中可用的设置类型及其默认值。
+ urls.py：Django项目的URL设置。可视其为你的Django网站的目录。目前它是空的。
+ wsgi.py：一个为你的Django项目提供兼容WSGI服务的接入点的文件（我完全不知道是什么）。查阅如何使用WSGI的更多细节（https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/）。

###运行开发服务器
为了安装后更多的体验Django，让我们运行一下Django的开发服务器看看我们的准系统。  

Django开发服务器是可用在开发期间的，一个内建的，轻量级的web服务。我们提供这个服务器是为了让你快速开发站点，也就是说在准备发布产品之前，无需进行产品级的web服务器（比如Apache）的配置工作。开发服务器检测你的代码并自动加载它，这样你会很容易修改代码而不用重启服务。  

如果你还没启动服务器的话，请切换到你的项目目录里（cd mysite），运行下边的命令：  
``python manage.py runserver``  
你会看到像这样的：  
- - -
Validating models...  
0 errors found.  

Django version 1.4.2, using settings 'mysite.settings'  
Development server is running at http://127.0.0.1:8000/（或者localhost:8000/）  
Quit the server with CONTROL-C.  
- - -
这将会在端口8000启动一个本地服务器，并且只能从你这台电脑连接和访问。既然服务器已经运行起来了，现在用网页浏览器访问 http://127.0.0.1:8000/ 。你应该可以看到一个令人赏心悦目的淡蓝色Django欢迎页面。它开始工作了。  

在进一步学习之前，一个重要的，关于开发网络服务器的提示很值得一说。虽然django自带的这个web服务器对于开发很方便，但是，千万不要在正式的应用部署环境中使用它。在同一时间，该服务器只能可靠的处理一次单个请求，并且没有进行任何类型的安全审计。发布站点前，请参阅第20章了解如何部署Django。

- - -
>更改 Development Server 的主机地址或端口  
>默认情况下，runserver命令在8000端口启动开发服务器，且仅监听本地连接。要想更改服务器端口的话，可将端口作为命令行参数传入：  
>``python manage.py runserver 8080``  
>通过指定一个IP地址，你可以告诉服务器-允许非本地连接访问。如果你想和其它开发人员共享同一开发站点的话，该功能特别有用。`0.0.0.0` 这个IP地址，告诉服务器去侦听任意的网络接口。  
>``python manage.py runserver 0.0.0.0:8000``  
>完成这些设置后，你本地网络中的其它计算机就可以在浏览器中访问你的IP地址了。比如：  
>http://192.168.1.103:8000/ 。（注意，你将需要校阅一下你的网络配置来决定你在本地网络中的IP地址）Unix用户可以在命令提示符中输入ifconfig来获取以上信息。使用Windows的用户，请尝试使用ipconfig命令。  

- - -

###接下来做什么？

好了，你已经安装好所需的一切，并且开发服务器也运行起来了，你已经准备好继续[学习基础知识-用Django伺候网页]()这一章的内容了  
