#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.

def users_login(request):
    return render(request,'users/login.html')

# 用户名验证
def user_name_ver(request):
    user = request.GET
    name=user.get('name')
    user_name = userInfo.objects.filter(user_name=name)
    if user_name == name:
        result = True
    else:
        result = False
    return HttpResponse(result)

# 密码验证
def user_passwd_ver(request):
    password = request.GET
   # print password
    passwd = password.get('passwd')
   # print passwd
    upassword = userInfo.objects.filter(upassword=passwd)
    print upassword

    if upassword == passwd:
        result = True
    else:
        result = False
    return HttpResponse(result)


def users_login_info(request):
    # 获取信息
    result = request.POST
    name = result.get('username')
    passwd= result.get('pwd')

    #在数据库中获取信息
    user_name = userInfo.objects.filter(user_name=name)
    upassword = userInfo.objects.filter(upassword=passwd)
    if user_name == name and upassword == passwd:
        return HttpResponse('登陆成功')
    else:
        return HttpResponse('用户或密码错误')

def users_register(request):
    return render(request,'users/register.html')

