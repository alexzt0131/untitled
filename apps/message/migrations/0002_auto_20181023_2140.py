# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-23 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.CharField(blank=True, default='', max_length=520, null=True, verbose_name='\u7559\u8a00\u4fe1\u606f'),
        ),
    ]