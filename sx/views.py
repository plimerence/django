#encoding=utf-8
from django.shortcuts import render,redirect
from .models import *
from hashlib import sha1
# Create your views here.
def register(request):
    return render(request,'user_info/register.html')


def register_handle(request):
    # 接收用户只
    post = request.POST
    umane = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    if upwd != upwd2:
       return  redirect('user/register/')

    s1 = sha1()
    print(type(upwd))
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()
    userinfo = userInfo()
    userinfo.uname = umane
    userinfo.upwd = upwd3
    userinfo.uemail = uemail
    userinfo.save()
    return  redirect('/user/login/')
def login(requst):
    return render(requst,'user_info/login.html')
