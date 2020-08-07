from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse, render, redirect


def index(reques):
    from app01 import models
    ret=models.User.objects.all()
    print(ret,type(ret))
    for i in ret:
        print(i,i.username,i.password)
    return  render(reques,'index.html')

def login(request):

    print(request,type(request))
    print(request.method,type(request.method))
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        #处理post请求--获取用户密码--校验状态--
        print(request.POST,type(request.POST))
        print(request.POST['user'],type(request.POST['user']))
        print(request.POST['pwd'],type(request.POST['pwd']))
        return render(request,'login.html')
def login1(request):
    from app01 import models

    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # if user == 'alex' and pwd == '123':
        if models.User.objects.filter(username=user,password=pwd):
            # return HttpResponse('登陆成功')
            return redirect('/index/')
    return render(request,'login2.html')


def index1(request):
    from app01 import models
    ret=models.User.objects.all()
    print(ret,type(ret))
    return  render(request,'index.html')