# python27-xadmin-imooc学习记录
视频编号3-5

## 一、windows7	python27 开发基础环境搭建

	python与模块版本：
		python2.7
		django1.9.8
		pip 最新
###1安装python2.7
	下载地址：https://www.python.org/download/releases/2.7.2/ 
	直接安装即可
###2设置环境变量
	在PATH中最后添加新安装python的路径如（c:\python27;C:\Python27\Scripts;）Scriptsm目录是模块执行的目录如virtualenv 模块pip、mkvirtualenv等，分号别忘记。
###3先安装setuptools
	下载地址：https://pypi.python.org/pypi/setuptools#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令：python setup.py install
###4安装pip 
	下载地址：https://pypi.python.org/pypi/pip#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令:python setup.py install 
###5安装virtualenv
	执行命令 pip install virtualenv
	如果找不到文件或者网络慢可使用国内的pip源地址
		
	阿里云 http://mirrors.aliyun.com/pypi/simple/
	
	中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
	
	豆瓣(douban) http://pypi.douban.com/simple/
	
	清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
	
	中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

	使用命令：pip install web.py -i http://pypi.douban.com/simple

	如果报错使用：pip install web.py -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

	如果想配置成默认的源，方法如下：
	
		需要创建或修改配置文件（一般都是创建），
		
		linux的文件在~/.pip/pip.conf，
		
		windows在%HOMEPATH%\pip\pip.ini），
		
		修改内容为：
		
		[global]
		index-url = http://pypi.douban.com/simple
		[install]
		trusted-host=pypi.douban.com
	
	
	新建虚拟环境：virtualenv d:\test4 提示结束后转到 test4目录下Script目录运行active激活当前虚拟环境，控制台符号变为(test4) d:\test4\Scripts>，如需退出执行deactive命令即可。
###6安装virtualenvwrapper
	由于virtualenv每次都要进入虚拟环境目录这样很麻烦所以需要安装virtualenvwrapper模块
	
	安装及使用方法：

	0.首先需要在系统变量中指定一个默认的WORKON_HOME的变量，即所有创建的虚拟环境的存放目录，如：d:\virtualnevs 注意不加冒号。（如果不能正常运行，就讲python安装目录中Script目录中的所有文件copy到指定的workon目录中）。
	
	1.安装虚拟环境

	pip install virtualenvwrapper-win ，linux可以去掉-win
	
	2.创建虚拟环境
	会在你当前用户下创建一个Env的文件夹，然后将这个虚拟环境安装到这个目录下
	
	mkvirtualenv 环境名称
	
	3.进入某个虚拟环境
	
	workon 环境名称
	
	4.退出当前环境
	
	deactivate
	
	5.列出全部虚拟环境
	
	lsvirtualenv
	
	6.删除某个虚拟环境
	
	rmvirtualenv 环境名称
	
	7.进入到虚拟环境所在的目录
	
	cdvirtualenv
#二、Django基础知识
##Django的目录结构
	需要新建几个目录：
		0.与工程名相同	存放工程文件的文件夹
		1.apps	  		存放web应用的文件夹
		2.log 	  		存放日志文件的文件夹
		3.static  		存放js、css及图片的文件夹
		4.media			存放用户上传文件的文件夹
		5.template		存放静态页面的文件夹

	在pycharm中可以将apps markdirectory as sourceroot，这样就可以在引入app中文件时不用添加apps了，不过在命令行中就会报错，解决方法是在settings.py中将apps文件夹设置为搜索目录。视频没演示，有待自行查询。
	
##Django与mysql的链接

	settings.py中设置：
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': '你的库名',
	        'USER': '账号',
	        'PASSWORD': '密码',
	        'HOST': '127.0.0.1',#本机可不改
	    }
	}
	数据库需要自己创建，django只会生成表。
	建好数据库使用manager命令 makemigrations -> migration来生成数据表
	
	**运行django工程时可能会发生的错误**
	#链接mysql数据库时报错，django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named MySQLdb
	#如果pip安装后还是提示这个错误，一定要先注意看安装MySQLdb用的是否是venv的python pip 不要用环境变量中的pip那样不会装到venv中，这个问题坑了我半个多小时。
	#win7下有可能会需要这两个dll拷贝到system32中：libguide40.dll、libmmd.dll
	#提供一个驱动下载的地址以防网络不好或者提示没有对应版本，注意python27 32位选win32的64选amd64的
	#https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
	
	

##静态文件的处理
	
	在settings中debug为true的情况下：
		例如引用static文件夹中的style.css文件页面上直接写入/static/css/style.css是无效的，需要在settings文件中增加一个列表
		STATICFILES_DIRS = [
		    os.path.join(BASE_DIR, 'static')
		]
		重启django这样就可以访问静态文件了。
	在settings.py中如果写了中文注释，python3没问题，python27需要再第一行加上#coding:utf-8	
#三、django orm与 model设计
##首先，先将我们的应用注册到django中

	在settings.py中的INSTALLED_APPS集合中添加刚生成的app,如果不添加migrate命令检测不到model的变化。
	例如:
		INSTALLED_APPS = [
		    'django.contrib.admin',
		    'django.contrib.auth',
		    'django.contrib.contenttypes',
		    'django.contrib.sessions',
		    'django.contrib.messages',
		    'django.contrib.staticfiles',
		    'apps.message'<-新添加的
		]
##model设计
	class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, default='', primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name="用户名")
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=120, null=True, blank=True, default='', verbose_name="联系地址")
    message = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name="留言信息")

    class Meta:
        verbose_name = "用户留言信息"
        verbose_name_plural = verbose_name #在djangoadmin中如果指定这个的话会显示verbose_name加s
        # 还可加一下的变量
        # db_table = 'user_message'
        # ordering = '-object_id'


##注册models
	在app文件夹中admin.py文件中使用一下方法注册（这样就可以在admin中管理）
	from models import UserMessage
	# Register your models here.
	
	admin.site.register(UserMessage)
##django model的增删改查
	def getFrom(request):
    ret = None
    if request.method == 'POST':
        reqs = request.POST
        print(reqs)
        oid = uuid.uuid4()
        name = reqs.get('name')
        email = reqs.get('email')
        message = reqs.get('message')
        address = reqs.get('address')
        #保存前台传来的请求数据
        UserMessage.objects.create(
            object_id=oid,
            name=name,
            email=email,
            message=message,
            address=address
        ).save()
        #从数据库中查询保存的数据
        umObj = UserMessage.objects.get(object_id=oid)
        print(umObj.name)
        print('*'*88)
        #使用过滤查询
        umObj1 = UserMessage.objects.filter(name=name, object_id=oid)#相当于and
        print(umObj1[0].name)
        print('*'*88)

         #将数据返回到前台
        ret = {
        'umObj1': umObj1[0],
        }
        print(ret)

    return render(request, 'form.html', ret)
	
	页面上需要的地方使用django模板语言来加载：{{ 变量名.属性名 }}如下例：
	<input value="{{ umObj1.name }}" id="name" type="text" name="name" class="error" placeholder="请输入您的姓名"/>

	删除方法比较简单，查询到需要删除的数据直接调用.delete方法就可以。

	修改也是要先实例化一个对象然后查出需要操作的数据直接 对象.属性 = 新属性 最后对象.save()

	Django路由方面的补充：
		在urls.py中定义urlpatterns列表中路由连接对应方法的时候可以设置一个name值，根据该值可以在模板处使用{% url '设置的name值' %}
		来直接获得到url的地址 比如：    url(r'^form/', views.getFrom, name="formPage"), 就可以或得到r'^form/'正则匹配的地址。这样
		在修改正则的时候就不用每个页面都修改了。
		更多django模板与filter需要学习一下，可以直接看Django的文档
