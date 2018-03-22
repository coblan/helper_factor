# encoding:utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField('学校名',max_length=200,blank=True)

class LClass(models.Model):
    name= models.CharField('班级名称',max_length=50,blank=True)
    
GEN=(
    ('male','男'),
    ('female','女')
)

class Student(models.Model):
    name = models.CharField('姓名',max_length=100,blank=True)
    age = models.CharField('年龄',max_length=20,blank=True)
    gender = models.CharField('性别',max_length=10,blank=True,choices=GEN)
    lclass = models.ForeignKey(LClass,verbose_name='班级',blank=True,null=True)
    head = models.CharField('头像',max_length=500,blank=True)
    start = models.DateField(verbose_name='入学日期',null=True,blank=True)
    
    def __unicode__(self):
        return self.name or '未命名'
    