# encoding:utf-8
from __future__ import unicode_literals
from helpers.director.shortcut import TablePage,ModelTable,page_dc,FieldsPage,ModelFields,model_dc
from django.contrib import admin
from .models import School,Student
# Register your models here.
class ScoolPage(TablePage):
    class tableCls(ModelTable):
        model=School
        exclude=[]

class SchoolFormPage(FieldsPage):
    class fieldsCls(ModelFields):
        class Meta:
            model=School
            exclude=[]

class StudentPage(TablePage):
    
    class tableCls(ModelTable):
        model=Student
        exclude=[]

class StudentFormPage(FieldsPage):
    class fieldsCls(ModelFields):
        class Meta:
            model=Student
            exclude=[]
        
        def dict_head(self, head):
            if head['name']=='head':
                head['type']='picture'
            return head
        

model_dc[School]={'fields':SchoolFormPage.fieldsCls}
model_dc[Student]={'fields':StudentFormPage.fieldsCls}

page_dc.update({
    'school.school':ScoolPage,
    'school.school.edit':SchoolFormPage,
    'school.student':StudentPage,
    'school.student.edit':StudentFormPage
})