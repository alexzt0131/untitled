##coding:utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default="", verbose_name="名称")
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
    mobile = models.CharField(max_length=11, null=True, verbose_name="手机号码")
    birday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="male", verbose_name="性别")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):#教程视频python2用__unicode__
        return self.username