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
##  ##实现流程
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
			`class UserProfile(AbstractUser):

			    nick_name = models.CharField(max_length=50, default='', verbose_name='昵称')
			    briday = models.DateField(null=True, blank=True, verbose_name='生日')
			    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="male")
			    address = models.CharField(max_length=100, default='')
			    mobile = models.CharField(max_length=11, null=True, blank=True)
			    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100, verbose_name='用户头像')
			
			    class Meta():
			        verbose_name = "用户信息"
			        verbose_name_plural = verbose_name
			
	    def __unicode__(self):
			        return self.username`
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
	`class Course(models.Model):
	
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
	    add_time = models.DateField(default=datetime.now(), verbose_name='添加时间')
	
	    class Meta():
	        verbose_name = "课程基本信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	`
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
	
	`class CityDict(models.Model):
	    name = models.CharField(max_length=100, verbose_name="城市名称")
	    desc = models.CharField(max_length=200, verbose_name="城市描述")
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "城市信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name
	
	
	class Oragnization(models.Model):
	
	
	    name = models.CharField(max_length=100, verbose_name="机构名称")
	    desc = models.CharField(max_length=200, verbose_name="机构描述")
	    click_num = models.IntegerField(default=0, verbose_name='点击人数')
	    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
	    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name='封面图')
	    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="机构地址")
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
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
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "教师基本信息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name`
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
	`'''
	用户咨询
	'''
	class UserAsk(models.Model):
	
	    name = models.CharField(max_length=100, verbose_name="姓名")
	    course = models.CharField(max_length=100, verbose_name="课程名称")
	    mobile = models.CharField(max_length=11, verbose_name='手机')
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "用户咨询"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name + self.course
	
	'''
	用户评论
	'''
	class CourseComments(models.Model):
	
	    name = models.CharField(max_length=100, verbose_name="用户")
	    course = models.CharField(max_length=100, verbose_name="课程")
	    comments = models.TextField(default='', verbose_name='留言')
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "用户评论"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.name + self.course
	
	'''
	用户收藏
	'''
	class UserFavorite(models.Model):
	
	    user = models.ForeignKey(UserProfile, verbose_name='用户')
	    fav_id = models.CharField(max_length=200, verbose_name='数据id')
	    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), default=1, verbose_name="收藏类型")
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "用户收藏"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.user + self.fav_id
	
	
	'''
	用户消息
	'''
	class UserMessage(models.Model):
	
	    user = models.IntegerField(default=0, verbose_name='接收用户id')#接受用户id（int型，默认为0,0为所有用户，非0既用户id）
	    message = models.TextField(default='', verbose_name='评论')
	    has_read = models.BooleanField(default=False, verbose_name="是否已读")
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "用户消息"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.user + self.has_read
	
	
	'''
	用户学习的课程
	'''
	class UserCourse(models.Model):
	    user = models.ForeignKey(UserProfile, verbose_name='用户')
	    course = models.ForeignKey(Course, verbose_name='课程')
	    add_time = models.DateField(default=datetime.now(), verbose_name='创建时间')
	
	    class Meta():
	        verbose_name = "用户学习的课程"
	        verbose_name_plural = verbose_name
	
	    def __unicode__(self):
	        return self.user`

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
## 5-5 xadmin全局配置 ##




##
