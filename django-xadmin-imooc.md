# python27-xadmin-imooc学习记录 #
视频编号5-1
# 一、windows7	python27 开发基础环境搭建 #

	python与模块版本：
		python2.7
		django1.9.8
		pip 最新
## 1安装python2.7 ##
	下载地址：https://www.python.org/download/releases/2.7.2/ 
	直接安装即可
## 2设置环境变量 ##
	在PATH中最后添加新安装python的路径如（c:\python27;C:\Python27\Scripts;）Scriptsm目录是模块执行的目录如virtualenv 模块pip、mkvirtualenv等，分号别忘记。
## 3先安装setuptools ##
	下载地址：https://pypi.python.org/pypi/setuptools#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令：python setup.py install
## 4安装pip ##
	下载地址：https://pypi.python.org/pypi/pip#downloads
	将下载后的tar文件解压，用CMD模式进入到解压后的文件所在的目录执行命令:python setup.py install 
## 5安装virtualenv ##
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
## 6安装virtualenvwrapper ##
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
# 二、Django基础知识 #
## Django的目录结构 ##
	需要新建几个目录：
		0.与工程名相同	存放工程文件的文件夹
		1.apps	  		存放web应用的文件夹
		2.log 	  		存放日志文件的文件夹
		3.static  		存放js、css及图片的文件夹
		4.media			存放用户上传文件的文件夹
		5.template		存放静态页面的文件夹

	在pycharm中可以将apps markdirectory as sourceroot，这样就可以在引入app中文件时不用添加apps了，不过在命令行中就会报错，解决方法是在settings.py中将apps文件夹设置为搜索目录。视频没演示，有待自行查询。
	
## Django与mysql的链接 ##

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
	
	

## 静态文件的处理 ##
	
	在settings中debug为true的情况下：
		例如引用static文件夹中的style.css文件页面上直接写入/static/css/style.css是无效的，需要在settings文件中增加一个列表
		STATICFILES_DIRS = [
		    os.path.join(BASE_DIR, 'static')
		]
		重启django这样就可以访问静态文件了。
	在settings.py中如果写了中文注释，python3没问题，python27需要再第一行加上#coding:utf-8	
# 三、django orm与 model设计 #
## 首先，先将我们的应用注册到django中 ##

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
## model设计 ##
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


## 注册models ##
	在app文件夹中admin.py文件中使用一下方法注册（这样就可以在admin中管理）
	from models import UserMessage
	
	admin.site.register(UserMessage)
## django model的增删改查 ##
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

# 四、 django app 设计（MOOC网站） #

## 模块分析0 ##
	**users-用户管理**
	**course-课程管理**
	**organization-机构和教师管理**
	**operation-用户操作管理**
## 实现流程 ##
**前期准备工作**
	0.开发环境选择
		django = 1.9.8
		python = 2.7

	1.django创建新项目
		projectname = mxonline
	2.配置数据库
		1）安装mysql驱动 pip install mysql-python
		2）配置settings.py中的databases，
		3）在mysql中创建一个mxonline的数据库
		4）使用djangoadmin命令生成数据库（makemigrations - migrate）
## modle设计 ##
**注意DateField都改为DateTimeField**
**1.User app**
	1）使用pycharm新建webapp Users
	2）创建User modle
		*扩展django Usermodle*
			定义UserProfile类集成AbstractUser来实现
			类中添加需要的字段（nick_name, birday, gender, address, mobile, image）
				gender只有两个选择可使用django模板中的choices
				models.CharField(max_length=5，choices=(("male","男"), ("female", "女")), default="male")
				image 用户头像图片
				models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)
				使用ImageField需要安装python pillow模块，使用pip install pillow即可
			定义 内部类 Meta
				定义verbose_name 与 verbose_name_plural，可查看django基础部分
				定义__unicode__方法为django admin 提供注册model的显示，python3 为__str__方法
			在定义AUTH_USER_MODEL = "users.UserProfile" #app名称+class名
			生成数据库（makemigrations - migrate）
	代码：
	'
	##coding:utf-8
	from __future__ import unicode_literals
	
	from datetime import datetime
	from django.contrib.auth.models import AbstractUser
	from django.db import models
	
	# Create your models here.
	
	class UserProfile(AbstractUser):
	
	    nick_name = models.CharField(max_length=50, default='', verbose_name='昵称')
	    briday = models.DateTimeField(null=True, blank=True, verbose_name='生日')
	    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="male")
	    address = models.CharField(max_length=100, default='')
	    mobile = models.CharField(max_length=11, null=True, blank=True)
	    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100, verbose_name='用户头像')
	
	    class Meta():
	        verbose_name = "用户信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.username
	
	
	class EmailVerifyRecord(models.Model):
	    code = models.CharField(max_length=20, verbose_name="验证码")
	    email = models.EmailField(max_length=50, verbose_name='邮箱')
	    send_type = models.CharField(choices=(('register', '注册'), ('forget', '忘记密码')), default='register', max_length=50, verbose_name='验证码类型')
	    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')
	
	    class Meta:
	        verbose_name = '邮箱验证码'
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return '{}({})'.format(self.code, self.email)
	
	
	class Banner(models.Model):
	    title = models.CharField(max_length=100, verbose_name="标题")
	    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图')
	    url = models.URLField(max_length=200, verbose_name='访问地址')
	    index = models.IntegerField(default=100, verbose_name='顺序')
	    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	
	    class Meta:
	        verbose_name = '轮播图'
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.title	
	'
**2.Course app**
	0)创建course modle

	1)**course 			- 课程基本信息**
		字段：
			name		课程名, 
			desc		课程描述, 
			detail		课程详情, 
			degree		课程级别（可用choices实现）, 
			learn_times	学习时长（分钟数int型）, 
			students	学习人数（int型），
			fav_nums	收藏人数（int型）, 
			image封面图（imageField）models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图"),
			click_nums	点击人数 （int型）,
			add_time	添加时间
		定义Meta内部类与__str__函数

	2)**lesson	-	章节信息**
			course 		课程 （外键）				
			name 		章节名
			add_time 	创建时间
		定义Meta内部类与__str__函数

	3)**video  			- 视频**
			lesson 		章节 （外键）				
			name 		视频名
		add_time 		创建时间
		定义Meta内部类与__str__函数

	4)**courseResource 	- 课程资源**
			course 		课程 （外键）		
			name 		名称
			download 	下载地址 models.FileField(upload_to="course/resource/%Y/%m", verbose_name="资源文件"， max_length=100)
			add_time 	创建时间
		定义Meta内部类与__str__函数
	代码：
	'
	##coding:utf-8
	import django
	from django.db import models
	
	from datetime import datetime
	# from django.utils.timezone import now
	#
	# print now()
	
	# Create your models here.
	class Course(models.Model):
	
	
	    name = models.CharField(max_length=100, verbose_name="课程名")
	    desc = models.CharField(max_length=200, verbose_name="课程描述")
	    detail = models.TextField(default='', verbose_name='课程详情')
	    degree = models.CharField(max_length=20,
	                              choices=(('base', '初级'), ('middle', '中级'), ('advance', '高级')),
	                              verbose_name='课程级别', default='base')
	    lern_times = models.IntegerField(default=0, verbose_name='学习时长')
	    students = models.IntegerField(default=0, verbose_name="学习人数")
	    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
	    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name='封面图')
	    click_num = models.IntegerField(default=0, verbose_name='点击人数')
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
	
	    class Meta():
	        verbose_name = "课程基本信息"
	        verbose_name_plural = verbose_name
	
	    # def __str__(self):
	    #     return self.name
	    def __unicode__ (self):
	        return self.name
	
	class Lesson(models.Model):
	    course = models.ForeignKey(Course, verbose_name="课程")
	    name = models.CharField(max_length=100, verbose_name='章节名')
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
	
	    class Meta():
	        verbose_name = "章节"
	        verbose_name_plural = verbose_name
	
	    # def __str__(self):
	    #     return self.name
	    def __unicode__ (self):
	        return self.name
	
	class Video(models.Model):
	    lesson = models.ForeignKey(Lesson, verbose_name="章节")
	    name = models.CharField(max_length=100, verbose_name='视频名')
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
	
	    class Meta():
	        verbose_name = "视频"
	        verbose_name_plural = verbose_name
	
	    # def __str__(self):
	    #     return self.name
	    def __unicode__ (self):
	        return self.name
	
	class CourseResource(models.Model):
	    course = models.ForeignKey(Course, verbose_name="课程")
	    name = models.CharField(max_length=100, verbose_name='名称')
	    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name='下载内容')
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='添加时间')
	
	    class Meta():
	        verbose_name = "课程资源"
	        verbose_name_plural = verbose_name
	
	    # def __str__(self):
	    #     return self.name
	    def __unicode__ (self):
	        return self.name	
	'
**3.organization app**
	0)创建 organization model
	
	1)**courseOrg 	-	课程机构基本信息**
		字段：
			name 		机构名称
			desc 		机构描述 （text类型）
			click_nums	点击数（int）
			fav_nums	收藏数（int）
			image		封面图（imageField）models.ImageField(upload_to="org/%Y/%m", verbose_name="封面图"),
			address		机构地址
			add_time 	创建时间
			city		所在城市 （外键）
		定义Meta内部类与__str__函数

	2)**teacher 	-	教师基本信息**
		字段：
			name 			教师姓名
			work_years		工作年限（int）	
			work_company	就职公司
			work_position 	公司职位
			course			课程（外键）~~~！！！！
			org 			所属机构（外键）
			points 			教学特点
			click_nums点击人数 （int型）
			add_time 	创建时间
			fav_nums	收藏数（int）
		定义Meta内部类与__str__函数

	3)**cityDict	-	城市信息**
		字段：
			name 		城市名称
			desc 		城市描述 
			add_time 	创建时间
		定义Meta内部类与__str__函数
	
	代码：
	'
	##coding:utf-8
	from __future__ import unicode_literals
	
	from django.db import models
	from datetime import  datetime
	# Create your models here.
	from course.models import Course
	
	
	class CityDict(models.Model):
	    name = models.CharField(max_length=100, verbose_name="城市名称")
	    desc = models.CharField(max_length=200, verbose_name="城市描述")
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "城市信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	
	
	class CourseOrg(models.Model):
	
	
	    name = models.CharField(max_length=100, verbose_name="机构名称")
	    desc = models.CharField(max_length=200, verbose_name="机构描述")
	    click_num = models.IntegerField(default=0, verbose_name='点击人数')
	    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
	    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name='封面图')
	    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="机构地址")
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
	    city = models.ForeignKey(CityDict, verbose_name='所在城市')
	
	    class Meta():
	        verbose_name = "课程机构基本信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	
	class Teacher(models.Model):
	
	    name = models.CharField(max_length=100, verbose_name="教师姓名")
	    work_yesrs = models.IntegerField(default=0, verbose_name='工作年限')
	    work_company = models.CharField(max_length=100, verbose_name="就职公司")
	    work_position = models.CharField(max_length=100, verbose_name="公司职位")
	    course = models.ForeignKey(Course, verbose_name='课程')
	    points = models.CharField(max_length=100, verbose_name="教学特点")
	    click_num = models.IntegerField(default=0, verbose_name='点击人数')
	    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "教师基本信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	'
**4.operation app**
	0)创建 operation model
	
	1)**userAsk			-	用户咨询**
		name		姓名
		mobile		手机号码
		course_name	课程名称
		add_time 	创建时间
	定义Meta内部类与__str__函数

	2)**courseComments	-	用户评论**
		user 		用户（外键）
		course		课程（外键）
		comments 	留言
		add_time 	创建时间
	定义Meta内部类与__str__函数

	3)**userFavorite 	-	用户收藏**
		user 		用户（外键）
		fav_id		数据id（收藏数据的id int型）
		fav_type	models.IntegerField(choices=((1,"课程"), (2, "课程机构"), (3， "讲师")), default=1, verbose_name="收藏类型")
		add_time 	创建时间
	定义Meta内部类与__str__函数

	4)**userMessage 	-	用户消息**
		user		接受用户id（int型，默认为0,0为所有用户，非0既用户id）
		message		评论
		has_read 	是否已读(布尔类型，默认false)			
		add_time 	创建时间
	定义Meta内部类与__str__函数

	5)**userCourse		-	用户学习的课程**
		user 		用户（外键）
		course		课程（外键）
			
		add_time 	创建时间
	定义Meta内部类与__str__函数
	
	代码：
	'
	##coding:utf-8
	from __future__ import unicode_literals
	
	from django.db import models
	from datetime import  datetime
	# Create your models here.
	from course.models import Course
	
	
	class CityDict(models.Model):
	    name = models.CharField(max_length=100, verbose_name="城市名称")
	    desc = models.CharField(max_length=200, verbose_name="城市描述")
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "城市信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	
	
	class CourseOrg(models.Model):
	
	
	    name = models.CharField(max_length=100, verbose_name="机构名称")
	    desc = models.CharField(max_length=200, verbose_name="机构描述")
	    click_num = models.IntegerField(default=0, verbose_name='点击人数')
	    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
	    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name='封面图')
	    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="机构地址")
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
	    city = models.ForeignKey(CityDict, verbose_name='所在城市')
	
	    class Meta():
	        verbose_name = "课程机构基本信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	
	class Teacher(models.Model):
	
	    name = models.CharField(max_length=100, verbose_name="教师姓名")
	    work_yesrs = models.IntegerField(default=0, verbose_name='工作年限')
	    work_company = models.CharField(max_length=100, verbose_name="就职公司")
	    work_position = models.CharField(max_length=100, verbose_name="公司职位")
	    course = models.ForeignKey(Course, verbose_name='课程')
	    points = models.CharField(max_length=100, verbose_name="教学特点")
	    click_num = models.IntegerField(default=0, verbose_name='点击人数')
	    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
	    add_time = models.DateTimeField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "教师基本信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	'

## 生成数据库表 ##

	**makemigrations -> migrate 创建表**创建apps文件夹将生成的app都移动到其中
	这时候需要将apps这个文件夹在pycharm中设置为sources Root,不然可能会引用不到其中的文件，这之后还要在settings.py中将apps文件夹插入进来加入一下代码即可：
		sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
	这样在引用这些app的时候就不用再前面加上apps了

# 第五章 通过xadmin快速搭建后台管理系统 #

## 5-1 django admin介绍 ##
** 修改系统语言为中 **
	修改django admin的语言为中文： 在settings.py中LANGUAGE_CODE = 'zh-hans' , ITME_ZONE = 'Asia/Shanghai'， USE_TZ = FALSE
**	注册model**
	注意：Django继承AbstractUser新建User Model时出现fields.E304错误需要在setting中重载AUTH_USER_MODEL
		settings.py中添加
		**AUTH_USER_MODEL = 'users.UserProfile'**


	1.admin.py中添加以下类：(不明白，以后查看）[question]
		class UserProfileAdmin(admin.ModelAdmin):
			pass
	2.使用admin.site.register(你的model) （以前用python3就是如此注册）
## 5-2 xadmin的安装 ##
	1.所在虚拟环境pip安装 xadmin，
		或者到github下载，下载文件拷贝到工程extra_apps中将此文件夹mark为source path直接调用就可以了，推荐这种方法
		这期间遇到了错误：
			from future.utils import iteritems
			ImportError: No module named future.utils
			解决方法：
				从github下载future的源码，将src/future文件夹拷贝到虚拟环境的Lib\site-packages\ 文件夹中
				git地址：https://github.com/PythonCharmers/python-future
		然后又报错：
		    import six
			ImportError: No module named six
			解决方法：
				pip install six
		最后在settings.py中加入sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

	2.在settings.py中注册xadmin与crispy-forms两个应用

	3.将url.py指向xadmin的url
		import xadmin
		urlpatterns = [
		    url(r'^admin/', admin.site.urls),#django admin
		    url(r'^xadmin/', xadmin.site.urls),#xadmin
		]

	4.取消原来的注册UserProfile model（xadmin会自动注册用户model）

	5.migrate生成xadmin的表

## 5-3 users app 的model注册 ##
	在需要注册的app中添加一个adminx.py的文件
	里面添加一个class 集成object
	如需在xadmin后台页面中指定显示该model的哪些列，
	需要再这个类中加上list_display字段赋值一个包含想显示字段列表）
	加入search_fields在后台启用搜索功能
	加入list_filter 来加入过滤器(有时间字段的时候非常有有用)

	class model名+Admin(object):
		pass
		list_display = [需要显示的字段1， 需要显示的字段2]
		search_fields = [需要搜索的字段1， 需要搜索的字段2]
		list_filter =  [所有字段]
	然后在使用xadmin.site.register(model名， 刚添加的类名)注册

	

## 5-4 剩余app model注册 ##
** opration、organization与course 和5-3的步骤以一样直接贴代码 **
	
	`import xadmin
	from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse
	
	
	
	class UserAskAdmin(object):
	    list_display = ['name', 'course', 'mobile', 'add_time']
	    search_fields = ['name', 'course', 'mobile']
	    list_filter = ['name', 'course', 'mobile', 'add_time']
	
	class CourseCommentsAdmin(object):
	    list_display = ['name', 'course', 'comments', 'add_time']
	    search_fields = ['name', 'course', 'comments']
	    list_filter = ['name', 'course', 'comments', 'add_time']
	
	class UserFavoriteAdmin(object):
	    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
	    search_fields = ['user', 'fav_id', 'fav_type']
	    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
	
	class UserMessageAdmin(object):
	    list_display = ['user', 'message', 'has_read', 'add_time']
	    search_fields = ['user', 'message', 'has_read']
	    list_filter = ['user', 'message', 'has_read', 'add_time']
	
	class UserCourseAdmin(object):
	    list_display = ['user', 'course', 'add_time']
	    search_fields = ['user', 'course']
	    list_filter = ['user', 'course', 'add_time']
	
	xadmin.site.register(UserAsk, UserAskAdmin)
	xadmin.site.register(CourseComments, CourseCommentsAdmin)
	xadmin.site.register(UserFavorite, UserFavoriteAdmin)
	xadmin.site.register(UserMessage, UserMessageAdmin)
	xadmin.site.register(UserCourse, UserCourseAdmin)
	`

	`import xadmin
	from .models import *
	
	class CourseAdmin(object):
	    list_display = ['name', 'desc', 'detail', 'degree', 'lern_times', 'students', 'fav_nums', 'image', 'click_num', 'add_time']
	    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_num']
	    list_filter = ['name', 'desc', 'detail', 'degree', 'lern_times', 'students', 'fav_nums', 'image', 'click_num', 'add_time']
	
	class LessonAdmin(object):
	    list_display = ['course', 'name', 'add_time']
	    search_fields = ['course', 'name']
	    list_filter = ['course', 'name', 'add_time']
	
	class VideoAdmin(object):
	    list_display = ['lesson', 'name', 'add_time']
	    search_fields = ['lesson', 'name']
	    list_filter = ['lesson', 'name', 'add_time']
	
	class CourseResourceAdmin(object):
	    list_display = ['course', 'name', 'download', 'add_time']
	    search_fields = ['course', 'name', 'download']
	    list_filter = ['course', 'name', 'download', 'add_time']
	
	xadmin.site.register(Course, CourseAdmin)
	xadmin.site.register(Lesson, LessonAdmin)
	xadmin.site.register(Video, VideoAdmin)
	xadmin.site.register(CourseResource, CourseResourceAdmin)`
	
	'
	import xadmin
	from .models import CityDict, CourseOrg, Teacher
	
	
	class CityDictAdmin(object):
	    list_display = ['name', 'desc', 'add_time']
	    search_fields = ['name', 'desc']
	    list_filter = ['name', 'desc', 'add_time']
	
	
	class CourseOrgAdmin(object):
	    list_display = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time']
	    search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city']
	    list_filter = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time']
	
	
	class TeacherAdmin(object):
	    list_display = ['name', 'work_yesrs', 'work_company', 'work_position', 'course', 'points', 'click_num', 'fav_nums', 'add_time']
	    search_fields = ['name', 'work_yesrs', 'work_company', 'work_position', 'course', 'points', 'click_num', 'fav_nums',]
	    list_filter = ['name', 'work_yesrs', 'work_company', 'work_position', 'course', 'points', 'click_num', 'fav_nums', 'add_time']
	
	xadmin.site.register(CityDict, CityDictAdmin)
	xadmin.site.register(CourseOrg, CourseOrgAdmin)
	xadmin.site.register(Teacher, TeacherAdmin)
	'

	

## 5-5 xadmin全局配置 ##
** 修改xadmin主题，顶部名称等 **
	
	from xadmin import views
	
	添加 BaseSetting类继承object
	class BaseSetting(object):
		enable_themes = True  #开启使用主题
		use_bootswatch = True #使用此选项需要使用网络，会有问题，详见 ** 遇到的问题 ** 2#
	
	注册 BaseSetting类
		xadmin.site.register(views.BaseAdminView, BaseSetting)

	
	添加 GlobalSettings类继承object
	class GlobalSettings(object):
		site_title = "你的title" #后台管理系统的主题
		site_footer = "footer" 		#下方的lable
		menu_style = 'accordion'	#使后台model列表可以折起
	注册GlobalSettings类继承object 类
		xadmin.site.register(views.CommAdminView, GlobalSettings)
	
** 未实现的 **
	自定义菜单显示顺序
	
	上面菜单的显示是根据我们注册的时间来显示的，我们可以自定义我们的菜单显示顺序：在users/adminx.py文件加上以下代码：
	
	
	from users.models import EmailVerifyRecord, Banner, UserProfile
	from courses.models import Course, CourseResource, Lesson, Video
	from organization.models import CourseOrg, CityDict, Teacher
	from operation.models import CourseComments, UserMessage, UserFavorite, UserCourse, UserAsk
	from django.contrib.auth.models import Group, Permission
	from xadmin.models import Log
	
	
	class GlobalSettings(object):
	    site_title = '慕学后台管理系统'
	    site_footer = '慕海学习网'
	    menu_style = 'accordion'
	
	    def get_site_menu(self):
	        return (
	                {'title': '课程管理', 'menus': (
	                    {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
	                    {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
	                    {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
	                    {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
	                    {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
	                )},
	                {'title': '机构管理', 'menus': (
	                    {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
	                    {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
	                    {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
	                )},
	                {'title': '用户管理', 'menus': (
	                    {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
	                    {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
	                    {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
	                    {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
	                    {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
	                )},
	
	                {'title': '系统管理', 'menus': (
	                    {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
	                    {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
	                    {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
	                    {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
	                    {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
	            )},)
	
	xadmin.site.register(views.CommAdminView, GlobalSettings)
	
	记住这段代码是和我们之前定义全局配置放在同一个函数里面的
	注意：是from users.models import EmailVerifyRecord, Banner, UserProfile而不是：from apps.users.models import EmailVerifyRecord, Banner, UserProfile
	
	RuntimeError: Model class apps.users.models.UserProfile doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
	
	也就是说直接from users.models，不用再写上from apps.users.models。




# 第6章用户注册功能实现 #


** 6-1 首页和登录页面的配置 **

	拷贝index.html,login.html页面到templates文件夹
	在urls.py中设置路由
		'
			from django.views.generic import TemplateView#使用此类as_view可以将html文件返回一个view
			
			urlpatterns = [
			    url(r'^admin/', admin.site.urls),#django admin
			    url(r'^xadmin/', xadmin.site.urls),#xadmin
			    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),#首页
			    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login')#登录
			]		
		'
	在settings.py中设置静态文件路径 
		'
			#配置静态文件地址
			STATICFILES_DIRS = (
			    os.path.join(BASE_DIR, 'static'),
			)
		'
	将静态文件拷贝到static文件夹中
	修改html页面中的连接，将静态文件的连接都改为/static/开头，可用替换批量操作
	修改页面中的超链接为刚设置好的路由即可。
** 6-2 ~ 6-3 用户登录 **
		1.在urls.py中设置路由
		urlpatterns = [
		    url(r'^admin/', admin.site.urls),#django admin
		    url(r'^xadmin/', xadmin.site.urls),#xadmin
		    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),#首页
		    # url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login')#登录
		    url(r'^login/$', views.userLogin, name='login'),#登录
		    url(r'^logout/$', views.userLogout, name='logout')#登出
		]
		
		2.由于需要用邮箱或者用户名都能登录，django自带的登录验证功能就不能满足需求了，需要自定义一个登录验证方法。
			1）在users.views中定义一个验证用的类继承ModelBackend，重写authenticate方法
			
				'
				from django.contrib.auth.backends import ModelBackend
				from django.db.models import Q
				class CustomBackend(ModelBackend):
				    '''
				    自定义登陆验证函数，替代django自带的登陆验证函数
				    '''
				    def authenticate(self, username=None, password=None, **kwargs):
				        try:
				            #查询用户是否存在
				            user = UserProfile.objects.get(Q(username=username) | Q(email=username))#用Q来多条件查询
				            if user.check_password(password):
				                # 验证成功返回用户
				                return user
				        except Exception as e:
				            # 验证失败返回none
				            print(e)
				            return None
				'
			2）在settings.py中重载一个变量AUTHENTICATION_BACKENDS为刚才创建的验证类，注意为类型元组单个值得时候别忘加逗号
				'
					#自定义的登陆验证
					AUTHENTICATION_BACKENDS = (
					    'users.views.CustomBackend',
					)

				'
			3）在users.views中添加userLogin方法
				
				'			
					from django.contrib.auth import authenticate, login, logout
					def userLogin(request):
					
					    if request.method == "POST":
					        username = request.POST.get('username', None)
					        password = request.POST.get('password', None)
					        user = authenticate(username=username, password=password)#如果重载了settings.py中的AUTHENTICATION_BACKENDS这个函数会自动调用
					        if user:
					            login(request, user)
					            return render(request, 'index.html')
					        else:
					            return render(request, 'login.html', {'msg': '用户登陆失败！'})
					    elif request.method == "GET":
					        return render(request, 'login.html', {})
				'
			4）在html页面中响应的修改，判断登录状态显示登录按钮或用户信息等。

		3.在users.views中添加userLogout方法
			'
				from django.contrib.auth import authenticate, login, logout
				def userLogout(request):
				
				    if request.method == "GET":
				        logout(request)
				        return render(request, 'index.html')
			'
			在html页面中将推出登录的连接指向此方法
	
** 6-4 ~ 6-5 用form实现登录 **

	*使用基于类的方法来实现登录
		1.在views中定义登录类 LoginView
		2.重写get与post函数，这两个函数相当于判断 if request.method == "POST":
		3.在其中写上业务逻辑
		4.在urls.py中引用并加上该类的路由以登录类为例 
			'from users.views import LoginView
			urlpatterns = [
			    url(r'^login/$', LoginView.as_view(), name='login'),#使用类的方式实现登录,需要加括号（）是调用
			]'
			

	*使用form来实现登录
		1.在app中新建forms.py文件
		2.引用from django import forms
		3.新建登录类继承forms.Form
			`from django import forms

			class LoginForm(forms.Form):
			    username = forms.CharField(required=True)
			    password = forms.CharField(required=True, min_length=5)`
		
		4.在views中登录类的对应函数中实例化登录form类，并在构造方法中传入提交方法对应的变量比如post函数
			`from forms import LoginForm
			def post(self, request):
				#生成表单实例,传入request.POST后会用form的成员变量与前台form中同样名称的input对应
	       	 	loginForm = LoginForm(request.POST)`
		5.使用 loginForm.is_valid()方法判断页面form填写是否合法，然后按照boolean值编写业务
	
		代码如下：
			'
			from forms import LoginForm
			class LoginView(View):
			    '''
			        使用类的方式来实现登录，只需重载get与post函数即可
			    '''
			    def get(self, request):
			        return render(request, 'login.html', {})
			
			    def post(self, request):
			        #生成表单实例,传入request.POST后会用form的成员变量与前台form中同样名称的input对应
			        loginForm = LoginForm(request.POST)
			        if loginForm.is_valid():#此函数检查LoginForm实现类中的限制是否通过
			            username = request.POST.get('username', None)
			            password = request.POST.get('password', None)
			            #使用自定义的验证函数CustomBackend
			            user = authenticate(username=username, password=password)
			            if user:
			                #如果用户存在，执行登录返回index页面
			                login(request, user)
			                return render(request, 'index.html')
			            else:
			                #如果用户不存在将错误信息返回到页面
			                return render(request, 'login.html', {'msg': '用户登陆失败！'})
			        else:
			            # 如果form表填写出错，将loginForm返回
			            return render(request, 'login.html', {'loginFrom': loginForm})
			'
			

** 6-6 session和cookie自动登录机制 **
	*理论知识
	
** 6-7 ~ 6-10 用户注册-1 **
	*配置注册页面路由

	    {#  href="{% url 'register' %}  可以获得urls.py中设置了name的url #}
	    <a style="color:white" class="fr registerbtn" href="{% url 'register' %}">注册</a>
	
		{% load staticfiles %}{# 这样就可以使用{% static 'uri' %} 来使用静态文件了 与直接使用/static/效果一样 #}
	    <link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">{# 改变服静态文件存放路径后的不用作修改操作 #}

	
	*使用django captcha 可以在from中添加一个叫CaptchaField的 Field
		https://github.com/mbi/django-simple-captcha #验证码生成	使用0.4.6
		文档地址：https://django-simple-captcha.readthedocs.io/en/latest/
		
		安装说明
	    Install django-simple-captcha via pip: pip install  django-simple-captcha
	
	    Add captcha to the INSTALLED_APPS in your settings.py
	
	    Run python manage.py migrate
	
	    Add an entry to your urls.py:
	
	    urlpatterns += [
	        url(r'^captcha/', include('captcha.urls')),
	    ]

	*定义Form

		在views.py中registerView中实例化Form并返回到页面
			'
				class RegisterForm(forms.Form):
				    email = forms.EmailField(required=True)
				    password = forms.CharField(required=True, min_length=5)
				    #使用验证Field
				    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})#定义验证码错误信息
			'
	
	*在页面中使用{{ registerForm.captcha }}{# 使用验证码 django captcha 生成 #}，点击更改验证码需要js完成
		'
		//刷新验证码
		function refresh_captcha(event){
		    $.get("/captcha/refresh/?"+Math.random(), function(result){
		        $('#'+event.data.form_id+' .captcha').attr("src",result.image_url);
		        $('#id_captcha_0').attr("value",result.key);
		    });
		    return false;
		}

		'

		django captcha原理：
			在页面中会自动生成一个hashkey 然后和数据库中作比对，如果有的话对比验证码
	
	*编写post注册逻辑，记得html页面中input的name要与Form类中的一致，才能验证。
		详见完整代码。

	*生成加密密码
		如果保存用户的时候不能直接保存明文需要加密处理，django中使用一下方法
			from django.contrib.auth.hashers import make_password
			make_password(password=password)

	*发送激活链接至用户邮箱
		验证逻辑是：
			使用之前创建的EmailVerifyRecord model 现将email存储，然后生成一个随机code保存到EmailVerifyRecord对象
			然后将code加到url链接中发送到用户邮箱，用户点击链接后从数据库中对应的EmailVerifyRecord对象中验证此code来
			实现邮箱验证的功能.
		apps中新建utils包，新建emailSend.py文件
		新建sendRegisterEmail方法
		使用django内置email模块发送邮件：
			from django.core.mail import send_mail
			新注册新浪邮箱：testdjangoemail@sina.com ， 密码 常用基础密码
			在邮箱中需要设置 POP3/SMTP服务与IMAP4服务/SMTP服务 的状态为 **开启	**		

			settings.py中设置
			'	
				EMAIL_HOST = 'smtp.sina.com'
				EMAIL_PORT = 25
				EMAIL_HOST_USER = 'testdjangoemail@sina.com'
				EMAIL_HOST_PASSWORD = 'password'
				EMAIL_USER_TLS = False
				EMAIL_FROM = "testdjangoemail@sina.com"
			'
		代码如下：
			'
				##coding:utf-8
				import random
				
				from testDjango.settings import EMAIL_FROM
				from users.models import EmailVerifyRecord
				from django.core.mail import send_mail
				
				def randonStr(rlength=32):
				    '''
				    生成随机字符的函数
				    :param rlength:字符长度
				    :return:
				    '''
				    result = ''
				    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
				    length = len(chars) - 1
				
				    for i in range(rlength):
				        result += chars[random.randint(0, length)]
				
				    return result
								
				
				def sendRegisterEmail(email, stype='register'):
				    '''
				    发送邮箱验证emal的函数
				    :param email:
				    :param type: 判断是注册还是找回密码
				    :return:
				    '''
				    code = randonStr()
				    emailRecord = EmailVerifyRecord()
				    emailRecord.code = code
				    emailRecord.email = email
				    emailRecord.send_type = stype
				    emailRecord.save()
				
				    #发送邮件使用django的内部函数来实现
				    email_title = ''
				    email_body = ''
				    '''
				    EMAIL_HOST = 'smtp.sina.com'
				    EMAIL_PORT = 25
				    EMAIL_HOST_USER = 'testdjangoemail@sina.com'
				    EMAIL_HOST_PASSWORD = 'Aa123456'
				    EMAIL_USER_TLS = False
				    EMAIL_FROM = "testdjangoemail@sina.com"
				    '''
				
				
				    #注册邮件
				    if stype == 'register':
				        email_title = '注册激活链接'
				        email_body = '点击链接激活账号：http://127.0.0.1:8000/active/{}'.format(code)
				        send_status = send_mail(
				            subject=email_title,
				            message=email_body,
				            from_email=EMAIL_FROM,
				            recipient_list=[email]
				                  )
				
				        if send_status:
				            #发送成功
				            pass
				        else:
				            #发送失败
				            pass
				
				    pass



			'
		views.py注册类中调用此函数
	
		在register.html中设置错误返回
	        <div class="error btns" id="jsEmailTips">{% for key,val in registerForm.errors.items %}{{ val }}{% endfor %}</div>
			相同与login.html也要设置一下错误之后input的样式，在各个包裹input的div的css样式中加上以下django模板语言
			{% if registerForm.errors.input的name %}errorput{% endif %}
			input将value的值回填到页面，这样即使用户输入错误跳转页面返回也不需要重新输入
            <input  type="text" id="id_email" name="email" value="{{ registerForm.email.value }}" placeholder="请输入您的邮箱地址" />

	*激活用户
		添加一个激活url
			*django 路由方面可以参考*
				https://blog.csdn.net/luanpeng825485697/article/details/79252182
	    	#通过url中正则传递参数的方式来获得参数，views中类get方法接收的时候需要加上一个与activeCode同名的形参
    		url(r'^active/(?P<activeCode>.*)/$', ActiveUserView.as_view(), name='userActive'), # 激活
			'
				class ActiveUserView(View):
			    '''
			        激活用户
			    '''
			
			    def get(self, request, activeCode):
			        print(activeCode)
			
			
			        return HttpResponseRedirect('/')

			'
		
	*登录逻辑中添加验证用户激活
		'
	        if user:
	       		#判断用户是否激活
	            if user.is_active:
	                #如果用户存在，执行登录返回index页面
	                login(request, user)
	                return render(request, 'index.html')
	        else:
	            return render(request, 'login.html', {'msg': '账号未激活'})
		'
	*完整代码：


		*注册类*
		'
			class RegisterView(View):
			    def get(self, request):
			        registerForm = RegisterForm()
			        return render(request, 'register.html', {'registerForm': registerForm})
			
		        def post(self, request):
			        #不要忘记传入request.POST
			        registerForm = RegisterForm(request.POST)
			        #前端form是否验证成功（这个from包含验证码）
			        if registerForm.is_valid():
			
			            email = request.POST.get('email', '')
			            #用email判断用户是否已经注册
			            if UserProfile.objects.filter(email=email):
			                #已注册
			                return render(request, 'register.html', {'registerForm': registerForm, 'msg': '用户已存在!'})
			            else:
			                #未注册
			
			                password = request.POST.get('password', '')
			                userProfile = UserProfile()
			                userProfile.email = email
			                userProfile.username = email
			                userProfile.password = make_password(password=password)
			                userProfile.is_active = False#表示用户还未通过邮箱激活
			                userProfile.save()
			                #发送激活链接
			
			                sendRegisterEmail(email=email, stype='register')
			
			
			                return HttpResponseRedirect('/login/')
			        else:
			            return render(request, 'register.html', {'registerForm': registerForm})

		'


		*激活用户类*
		'
			class ActiveUserView(View):
		    '''
		        激活用户
		    '''
		
		    def get(self, request, activeCode):
		        #查询code是否存在
		        allRecords = EmailVerifyRecord.objects.filter(code=activeCode)
		        if allRecords:
		            for record in allRecords:
		                #查询此记录的email，通过email获得用户设置状态为激活然后保存
		                email = record.email
		                user = UserProfile.objects.get(email=email)
		                user.is_active = True
		                user.save()
		        else:
		            #告知用户激活失败
		            return HttpResponse('<h1>连接失效</h1>')
		        #重定向到login页面
		        return HttpResponseRedirect('/login/')
		'


		*添加验证激活后的登录类*
		'
			class LoginView(View):
		    '''
		        使用类的方式来实现登录，只需重载get与post函数即可
		    '''
		
		    def get(self, request):
		        return render(request, 'login.html', {})
		
		    def post(self, request):
		
		
		        #生成表单实例,传入request.POST后会用form的成员变量与前台form中同样名称的input对应
		        loginForm = LoginForm(request.POST)
		        if loginForm.is_valid():#此函数检查LoginForm实现类中的限制是否通过
		            username = request.POST.get('username', None)
		            password = request.POST.get('password', None)
		            #使用自定义的验证函数CustomBackend
		            user = authenticate(username=username, password=password)
		            if user:
		                # # 如果用户存在，执行登录返回index页面
		                # login(request, user)
		                # return render(request, 'index.html')
		                #判断用户是否激活
		                if user.is_active:
		                    #如果用户存在，执行登录返回index页面
		                    login(request, user)
		                    return render(request, 'index.html')
		                else:
		                    return render(request, 'login.html', {'msg': '账号未激活'})
		            else:
		                #如果用户不存在将错误信息返回到页面
		                return render(request, 'login.html', {'msg': '用户登陆失败！'})
		        else:
		            # 如果form表填写出错，将loginForm返回
		            return render(request, 'login.html', {'loginFrom': loginForm})

		'

** 6-11 ~ 6-12 找回密码 **
	
	*将forgetpwd.html拷贝到template中
		修改静态文件地址
	*在views中定义ForgetPwdView，渲染forgetpwd.html，并配置路由
		'	
	    url(r'forget/$', views.ForgetPwdView.as_view, name='forget'), #忘记密码页面
		
		class ForgetPwdView(View):

		    def get(self, request):
		
		        return render(request, 'forgetpwd.html')
		'
	
	*在login页面中将忘记密码连接指向forget

	*在forms.py中添加RestPwdForm
		'
		class ForgetForm(forms.Form):
		    email = forms.EmailField(required=True)
		    # 使用验证Field
		    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})  # 定义验证码错误信息
		'
	*修改ForgetPwdView将ForgetForm返回到页面forgetpwd.html实现验证码功能
		修改一下get方法即可
			'
		    def get(self, request):
		        forgetForm = ForgetForm()
		        return render(request, 'forgetpwd.html', {"forgetForm": forgetForm})
			'
		html中相应位置添加{{ forgetForm.captcha }}

	*编写ForgetPwdView中的post函数
		验证表单合法性
		获得html页面提交的email
		发送验证邮件
		'
	    def post(self, request):
	        #获得form对象并验证前天填写是否合法
	        forgetForm = ForgetForm(request.POST)#!!!!!!!!!千万不要忘记填写request.POST
	        if forgetForm.is_valid():
	            #获得email
	            email = request.POST.get('email', '')
	            #发送验证邮件
	            sendRegisterEmail(email=email, stype='forget')
	            return HttpResponse('邮件发送成功，前往邮箱重置密码。')
	        else:
	            return render(request, 'forgetpwd.html', {"forgetForm": forgetForm})
		'
		html中设置根据表单是否有错显示错误css与用户输入的回显
			'
			<div class="form-group marb20 {% if forgetForm.errors.email %}errorput{% endif %}">
                <label>帐&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
                <input type="text" id="account" name="email" value={{ forgetForm.email.value }} placeholder="邮箱" />
            </div>
			'
	
	*将password_reset.html拷贝到template文件夹，设置url路由
		'
	    url(r'^reset/(?P<resetCode>.*)/$', views.ResetView.as_view(), name='resetPwd'), # 找回密码
		'	

	*views中添加修改密码的ResetView类
		接收邮件内重置密码的code，通过EmailVerifyRecord对象获得email
		将email返回到修改密码页面password_reset.html,post中找回逻辑需要根据email找到用户

	*添加密码修改form类
		'
		class ModifyPwdForm(forms.Form):
		    password = forms.CharField(required=True, min_length=5)
		    password2 = forms.CharField(required=True, min_length=5)
		'
	*修改密码的POST要提交到一个新的连接resetPwd的连接需要提交一个resetCode，需要新建一个不要提供code的url，相应的类也是要新建。
		
		新建url
			'
    		url(r'^modifyPwd/$', views.ModifyPwd.as_view(), name='modifyPwd'), # 修改密码
			'		
		将password_reset.html form中的action改为新的url
		views编写ModifyPwd类实现post方法处理提交的密码
			'
			class ModifyPwd(View):
			    '''
			    因password_reset提交到post携带不了code，ResetView的url不适用所以才新建此类
			    '''
			    def post(self, request):
			        #获得form表单
			        modifyPwdForm = ModifyPwdForm(request.POST)##别忘记参数
			        email = request.POST.get('email', '')
			        rpwd = None
			        #判断前台form是否合法
			        if modifyPwdForm.is_valid():
			            pwd = request.POST.get('password', '')
			            pwd2 = request.POST.get('password2', '')
			
			            #判断密码是否一样
			            if pwd != pwd2:
			                return render(request, 'password_reset.html', {'email': email, 'msg': '密码不一致'})
			            else:
			                #找到user
			                user = UserProfile.objects.get(email=email)
			                user.password = make_password(password=pwd)
			                user.save()
			                # 重定向到login页面
			                return HttpResponseRedirect('/login/')
			        else:
			            return render(request, 'password_reset.html', {'email': email, 'modifyPwdForm': modifyPwdForm})
			'
	
	*未实现

		code过期，单次使用。


# 第7章课程机构功能实现 #
** 7-1 ~ 7-2 django templates模板继承 **
	*将org-list.html拷贝到template文件夹中
	*定义org_list的url
		'
	    #课程机构首页
    	url(r'^org_list/$', OrgView.as_view(), name='org_list'),
		'
	*新建base.html文件，将org-list.html的内容拷贝到其中
	*将需要继承的位置用{% block block名 %} {% endblock %}包裹起来，比如说header和footer
	*在org-list.html页面使用{% extends 'base.html' %}
	*由于base页面有使用static关键字的内容所以继承的页面中也需要引入{% load staticfiles %}
	*使用{% block block名 %} {% endblock %}来修改block中的内容

** 7-3 ~ 7-4 课程机构列表页数据展示 **
	*在xadmin中添加数据
		添加城市信息
		在添加图片的时候还需要在settings.py中设置media文件夹的URL
			'
			#media文件存放地址
			MEDIA_RUL = '/media/'
			MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

			'	
		这样在models中设计的如：
    		image = models.ImageField(upload_to="org/%Y/%m", verbose_name='封面图')
			设置upload_to属性才会将文件存到media文件夹中

			** ImageField在数据库中存储的是文件的相对路径，引用方法如下：**
				1.设置MEDIA_URL 与 MEDIA_ROOT 路径
				2.settings.py的TEMPLATES中的context_processors添加一个media的django处理类'django.core.context_processors.media'这样django就会将media的路径注册到html中
				3.urls.py中设置上传文件夹media的处理函数
					'
					from django.views.static import serve
				    #配置media文件处理
    				url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
					'
				4.html中引用的时候{{ MEDIA_URL }}{{ 含有ImageField属性的对象.image }}
				


	*由于课程机构内没有区分机构类别的属性，现在补上一个。
		'category = models.CharField(max_length=20, choices=(('pxjg', "培训机构"), ('gx', '高校'), ('gr', '个人')), verbose_name='机构类别', default='pxjg')'
		
		migrate 更新数据库
		
	*OrgView中查询所有机构与城市数据并返回到org-list.html页面中
		
		OrgView
		'
		class OrgView(View):
		    def get(self, request):
		        all_orgs = CourseOrg.objects.all()
		        all_cities = CityDict.objects.all()
		        ret = {
		            'all_orgs': all_orgs,
		            'all_cities': all_cities
		        }
		        return render(request, 'org-list.html', ret)
		'
		html
			'
			<li>
				<h2>所在地区</h2>
				<div class="more">更多</div>
				<div class="cont">
	                <a href="?ct="><span class="active2">全部</span></a>
	                        {% for city in all_cities %}
	                            <a href="?city=1&ct="><span class="">{{ city.name }}</span></a>
	                        {% endfor %}
				</div>
			</li>
			'
** 7-5 列表分页功能 **
	*使用django-pure-pagination分页库

		地址：https://github.com/jamespacileo/django-pure-pagination

	*pip安装：
		pip install django-pure-pagination

	*在settings.py中配置
		'
		INSTALLED_APPS = (
		    ...
		    'pure_pagination',
		)
		'
		可选设置
		'
		PAGINATION_SETTINGS = {
		    'PAGE_RANGE_DISPLAYED': 10,
		    'MARGIN_PAGES_DISPLAYED': 2,
		
		    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
		}
		'

	
	*按分页显示OrgView
		'
		class OrgView(View):
		    def get(self, request):
		        #所有课程和城市
		        all_orgs = CourseOrg.objects.all()
		        all_cities = CityDict.objects.all()
		        org_nums = all_orgs.count()
		
		        #分页获得所有机构
		        #获得页码的代码，没有获得1
		        try:
		            page = request.GET.get('page', 1)
		        except PageNotAnInteger:
		            page = 1
                #Paginator函数,object_list为所有的obj，per_page为每页显示数量
		        p = Paginator(object_list=all_orgs, per_page=5, request=request)
		        #按per_page分页返回到页面
		        orgs = p.page(page)
		
		        #返回到页面的数据
		        ret = {
		            'all_orgs': orgs,
		            'all_cities': all_cities,
		            'org_nums': org_nums
		        }
		        return render(request, 'org-list.html', ret)
		'

	*html中的代码
		'
		<div class="pageturn">
            {# 使用paginator自带的渲染 {{ all_orgs.render }} #}
            <ul class="pagelist">
                {# 判断是否有前页 #}
                {% if all_orgs.has_previous %}
                    <li class="long"><a href="?{{ all_orgs.previous_page_number.querystring }}">上一页</a></li>
                {% endif %}

                {# 分页显示 #}
                {% for page in all_orgs.pages %}
                    {% if page %}
                        {% ifequal page all_orgs.number %}
                            <li class="active"><a href="javascript:void(0);">{{ page }}</a></li>
                        {% else %}
                            <li><a href="?{{ page.querystring }}" class="page">{{ page }}</a></li>
                        {% endifequal %}
                    {% endif %}
                {% endfor %}

                {# 判断是否有后页 #}
                {% if all_orgs.has_next %}
                    <li class="long"><a href="?{{ all_orgs.next_page_number.querystring }}">下一页</a></li>
                {% endif %}
            </ul>

        </div>
		'
	
** 7-6 列表筛选功能 **
** 7-7 modelform提交我要学习咨询1 **
** 7-8 modelform提交我要学习咨询2 **
** 7-9 机构详情展示-1 **
** 7-10 机构详情展示-2 **
** 7-11 机构详情展示-3 **
** 7-12 课程机构收藏功能 ** 


# 遇到的问题 #
** 1.Error fetching command 'collectstatic': You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path. **
	解决（搜索到的方式）：修改settings.py中STATIC_ROOT为你的static静态文件的物理路径，比如说我静态文件存放在/home/user/www/static中，首先创建www目录下的static文件夹，最后修改settings.py中STATIC_ROOT指向/home/user/www/static。
	（视频给的方式）： 未获得
** 2.使用use_bootswatch = True xadmin主题的时候无法获取其他主题**
	解决：
		原文地址：https://blog.csdn.net/fanlei5458/article/details/80616296
		xadmin采用源代码的方式引入到项目中

		在xadmin使用的过程中，设置“use_bootswatch = True”，企图调出主题菜单，显示更多主题。然而设置了后，发现主题还是默认和bootstrap2，深入跟踪源代码，发现/xadmin/plugins/themes.py下的
		
		block_top_navmenu
		当use_bootswatch 为True的时候，就会使用httplib2去
		
		http://bootswatch.com/api/3.json
		网址获取主题菜单项。但是使用浏览器打开这个网址，http会被替换成https的。httplib2访问这个https的网址，就会报错。报错信息为：
		
		[SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure
		这边使用requests库来替代httplib2.
		1.安装requests
			pip install requests
		2.在./xadmin/plugins/themes.py 引入requests
			import requests
		3.修改block_top_navmenu方法：
		
		block_top_navmenu代码
		'
	    def block_top_navmenu(self, context, nodes):

	        themes = [
	            {'name': _(u"Default"), 'description': _(u"Default bootstrap theme"), 'css': self.default_theme},
	            {'name': _(u"Bootstrap2"), 'description': _(u"Bootstrap 2.x theme"), 'css': self.bootstrap2_theme},
	            ]
	        select_css = context.get('site_theme', self.default_theme)
	
	        if self.user_themes:
	            themes.extend(self.user_themes)
	
	        if self.use_bootswatch:
	
	            ex_themes = cache.get(THEME_CACHE_KEY)
	            if ex_themes:
	                themes.extend(json.loads(ex_themes))
	            else:
	                ex_themes = []
	                try:
	                    flag = False  # 假如为True使用原来的代码，假如为Flase，使用requests库来访问
	                    if flag:
	                        h = httplib2.Http()
	                        resp, content = h.request("https://bootswatch.com/api/3.json", 'GET', '',
	                                                  headers={"Accept": "application/json",
	                                                           "User-Agent": self.request.META['HTTP_USER_AGENT']})
	                        if six.PY3:
	                            content = content.decode()
	                        watch_themes = json.loads(content)['themes']
	                    else:
	                        content = requests.get("https://bootswatch.com/api/3.json")
	                        if six.PY3:
	                            content = content.text.decode()
	                        watch_themes = json.loads(content.text)['themes']
	                    ex_themes.extend([
	                        {'name': t['name'], 'description': t['description'],
	                         'css': t['cssMin'], 'thumbnail': t['thumbnail']}
	                        for t in watch_themes])
	                except Exception as e:
	                    print(e)
	
	                cache.set(THEME_CACHE_KEY, json.dumps(ex_themes), 24 * 3600)
	                themes.extend(ex_themes)
	
	        nodes.append(
	            loader.render_to_string('xadmin/blocks/comm.top.theme.html', {'themes': themes, 'select_css': select_css}))
** 3. 全局变量设置后台model显示中文时：RuntimeError: Model class users.models.UserProfile doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS. **

	如果已经mark了apps文件夹做sourcepath，需要注意在引用的时候不要from apps.appname... import ... 要把第一个apps去掉
	还要注意每个app的apps.py中
	class UsersConfig(AppConfig):
    	name = 'users'#这个一定不要加apps
		'

** 4.在html中引用上传到media文件夹中的图片的方法 **

		在settings.py中配置
		'		
		#media文件存放地址
		MEDIA_RUL = '/media/'
		MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

		'	

		这样在models中设计的如：
    		image = models.ImageField(upload_to="org/%Y/%m", verbose_name='封面图')
			设置upload_to属性才会将文件存到media文件夹中

		** ImageField在数据库中存储的是文件的相对路径，引用方法如下：**
			1.设置MEDIA_URL 与 MEDIA_ROOT 路径
			2.settings.py的TEMPLATES中的context_processors添加一个media的django处理类'django.core.context_processors.media'这样django就会将media的路径注册到html中
			3.urls.py中设置上传文件夹media的处理函数
				'
				from django.views.static import serve
			    #配置media文件处理
				url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
				'
			4.html中引用的时候{{ MEDIA_URL }}{{ 含有ImageField属性的对象.image 