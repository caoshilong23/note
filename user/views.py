import hashlib

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from .models import User


# Create your views here.


def login(request):
    if request.method == 'GET':
        if request.session.get('username') and request.session.get('uid'):
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')

        c_username = request.COOKIES.get('username')
        c_uid = request.COOKIES.get('uid')
        if c_username and c_uid:
            request.session['username'] = c_username
            request.session['uid'] = c_uid
            # return HttpResponse('已登录')
            return HttpResponseRedirect('/index')
        return render(request, 'user/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            use = User.objects.get(username=username)
        except Exception as e:
            print('login user is error %s' % e)
            return HttpResponse('用户名或密码错误')

        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        if use.password != password_m:
            return HttpResponse('用户名或密码错误')
        request.session['username'] = username
        request.session['uid'] = use.id
        resp = HttpResponseRedirect('/index')
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600*24*3)
            resp.set_cookie('uid', use.id, 3600*24*3)
        return resp


def logon(request):
    if request.method == 'GET':
        return render(request, 'user/logon.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        # 判断两次密码是否一致
        if password != password_2:
            return HttpResponse('两次密码不一致')
        # 判断账户是否存在
        db_user = User.objects.filter(username=username)
        if db_user:
            return HttpResponse('用户名已存在')
        # 密码加密
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        # 存储数据
        try:
            user = User.objects.create(username=username, password=password_m)
        except Exception as e:
            print('--create user error :%s' % e)
            return HttpResponse('用户名已存在')
        request.session['username'] = username
        request.session['uid'] = user.id
        return HttpResponseRedirect('/index')



def logout(request):
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']

    resp = HttpResponseRedirect('/index')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    if 'uid' in request.COOKIES:
        resp.delete_cookie('uid')
    return resp
