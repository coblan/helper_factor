# encoding:utf-8

from __future__ import unicode_literals
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine,page,fa,can_list,can_touch
from django.contrib.auth.models import User,Group
from helpers.maintenance.update_static_timestamp import js_stamp

class PcMenu(BaseEngine):
    url_name='helper'
    brand = 'helper_重构'
    menu=[
        
        #{'label':'学校','url':page('school.school'),'icon':fa('fa-home')},
        
        {'label':_('学校管理'),'icon':fa('fa-users'),'visible':can_list((User,Group)),
        'submenu':[
            {'label':'学校管理','url':page('school.school'),'visible':can_touch(User)},
            {'label':'学生管理','url':page('school.student'),'visible':can_touch(Group)},
            ]},
    
        #{'label':'首页','url':page('home'),'icon':fa('fa-home')},
        # {'label':'政策','icon':fa('fa-sitemap'),'submenu':[
            # {'label':'政策协议','url':page('liantang.policy')},
            # {'label':'申请表格','url':page('liantang.applytable')}
            # ]},
        
        #{'label':'政策协议','url':page('liantang.policy'),'icon':fa('fa-sitemap')},
        #{'label':'申请表格','url':page('liantang.applytable'),'icon':fa('fa-life-ring')},
        #{'label':'建房信息','url':page('liantang.jianfanginfo'),'icon':fa('fa-building')},
        ## {'label':'GIS区域','url':page('geoinfo.blockpolygon'),'icon':fa('fa-map-o')},
        ## {'label':'区域组','url':page('geoinfo.blockgroup'),'icon':fa('fa-map-o')}
        #{'label':'村委信息','url':page('liantang.cunwei'),'icon':fa('fa-life-ring')},
        
        ##{'label':'账号管理','url':page('user'),'icon':fa('fa-users')},
         {'label':'账号','url':page('user'),'icon':fa('fa-users'),'visible':can_list((User,Group)),
              'submenu':[
                  {'label':'账号管理','url':page('user'),'visible':can_touch(User)},
                  {'label':'权限分组','url':page('group_human'),'visible':can_touch(Group)},
            ]},        
        
    ]
    
    def custome_ctx(self, ctx):
        ctx['js_stamp']=js_stamp
        ctx['table_fun_config'] ={
            'detail_link': '详情', #'<i class="fa fa-info-circle" aria-hidden="true" title="查看详情"></i>'#,
        }
        return ctx      

PcMenu.add_pages(page_dc)