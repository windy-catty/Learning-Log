"""定义users的URL模式"""

from django.urls import path,re_path
from django.contrib.auth.views import LoginView

from . import views

app_name='users'

urlpatterns = [
    #登录页面
    re_path(r'^login/$',LoginView.as_view(template_name='users/login.html'),name='login'),
    #注销
    re_path(r'^logout/$',views.logout_view,name='logout'),
    #注册页面
    re_path(r'^register/$',views.register,name='register'),
]