#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from hashlib import sha1
# Create your views here.

def users_login(request):
    return render(request,'users/login.html')

# 用户名验证
def user_name_ver(request):
    #print '===='
    user = request.GET
    name=user.get('name')
   # print '====='
   # print name
    user = userInfo.objects.filter(user_name=name).count()
    return JsonResponse({'result':user})

# 密码验证
def user_passwd_ver(request):
    password = request.GET
    name = password.get('name')
    lens = len(name)
    passwd = password.get('passwd')
    s1 = sha1()
    s1.update(passwd)
    upasswd_sha1 = s1.hexdigest()
    count = userInfo.objects.filter(upassword=upasswd_sha1).count()
    if count > 1 and lens != 0:
        result = 1
    else:
        result = 0
    #print result
    return JsonResponse({'result':result})


def users_login_info(request):
    # 获取信息
    result = request.POST
    bools = result.get('jizhu')
    print bools
    user = result.get('username')
    print user
    print "++++++"
    passwd = result.get('pwd')
    print passwd
    s1 = sha1()
    s1.update(passwd)
    upasswd_sha1 = s1.hexdigest()
    print upasswd_sha1
    response = HttpResponse()
    print "-------++"
    print response
    print '++++----'
    if bools == 'True':
        print '------'
        response.set_cookie('users', value=user, max_age=None, expires=None)
        context = 'ok'
    else:
        #request.COOKIES['users']
        response.delete_cookie('users')
        context = 'no'
    return HttpResponse('ok')


#注册页面
def users_register(request):
    return render(request,'users/register.html')

# 注册验证
def users_register_ver(request):
    name = request.GET.get('uname')
    print name
    count = userInfo.objects.filter(user_name = name).count()

    return JsonResponse({'nums':count})


# 提交注册
def users_register_commit(request):
    #print '====='
    result = request.POST
    uname = result.get('user_name')
    upasswd = result.get('pwd')
    upasswdd = result.get('cpwd')
    uemail = result.get('email')
    uallow = result.get('allow')

    if upasswd == upasswdd:
        # 加密
        s1 = sha1()
        s1.update(upasswd)
        upasswd_sha1 = s1.hexdigest()
        print upasswd_sha1
        user = userInfo()
        user.user_name = uname
        print user.user_name
        user.upassword = upasswd_sha1
        print user.upassword
        user.umail = uemail
        print user.umail
        user.save()
    return redirect('/users/')


