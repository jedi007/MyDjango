from django.urls import path,re_path#导入re_path即可匹配正则

from . import views

app_name='gobang'#在django2 中必须添加appname,否则urls.py中无法使用include包含namespace

urlpatterns = [
    path('index/', views.index), 
    path('py_step/', views.py_step,name='py_step'), 
]
