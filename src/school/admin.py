# encoding:utf-8
from __future__ import unicode_literals
from helpers.director.shortcut import TablePage,ModelTable,page_dc
from django.contrib import admin
from .models import School
# Register your models here.
class ScoolPage(TablePage):
    class tableCls(ModelTable):
        model=School
        exclude=[]
    
page_dc.update({
    'school.school':ScoolPage,
    
})