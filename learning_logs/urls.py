"""定义learning_logs的URL模式"""

from django.urls import path,re_path

from . import views

app_name='learning_logs'

urlpatterns = [
    #主页
    re_path(r'^$',views.index,name='index'),
    
    #显示所有的主题
    re_path(r'^topics/$',views.topics,name='topics'),
    
    #显示所有的公开主题
    re_path(r'^public_topics/$',views.public_topics,name='public_topics'),
    
    #特定主题的详细页面
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    
    #用于添加新主题的网页
    re_path(r'^new_topics/$',views.new_topic,name='new_topic'),
    
    #用于删除新主题的网页
    re_path(r'^delete_topics/(?P<topic_id>\d+)/$',views.delete_topic,name='delete_topic'),
    
    #用于修改既有主题的公开状态的网页
    re_path(r'^public_topic/(?P<topic_id>\d+)/$',views.public_topic,name='public_topic'),
    
    #用于添加新条目的页面
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    
    #用于编辑既有条目的页面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
]