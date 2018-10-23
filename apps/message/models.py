##coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, default='', primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name="用户名")
    email = models.EmailField(verbose_name='邮箱')
    address = models.CharField(max_length=120, null=True, blank=True, default='', verbose_name="联系地址")
    message = models.CharField(max_length=520, null=True, blank=True, default='', verbose_name="留言信息")

    class Meta:
        verbose_name = "用户留言信息"
        verbose_name_plural = verbose_name #在djangoadmin中如果指定这个的话会显示verbose_name加s
        # 还可加一下的变量
        # db_table = 'user_message'
        # ordering = '-object_id'

    def __str__(self):
        return '{}-{}-{}'.format(self.object_id, self.name, self.message)