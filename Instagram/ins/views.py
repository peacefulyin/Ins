#coding=utf-8
import random

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import InsArticle, InsUser


def index(request):
    articles = InsArticle.objects.all().order_by('-pub_time')
    pagenator = Paginator(articles,10)
    context = {'page':pagenator.page(1)}

    return render(request, 'ins/index.html', context)


def blog(request):
    return render(request, 'ins/blog.html')

def login(request):
    return render(request, 'ins/login.html')


def home(request):
    return render(request, 'ins/home.html')


def edit(request):
    return render(request, 'ins/edit.html')

def chpass(request):
    return render(request, 'ins/chpass.html')


def manage_access(request):
    return render(request, 'ins/manage_access.html')

def comment_filter(request):
    return render(request, 'ins/comment_filter.html')

def email_set(request):
    return render(request, 'ins/email_set.html')

def contact_history(request):
    return render(request, 'ins/contact_history.html')

def explore_people(request):
    expore_users = InsUser.objects.all()
    random_user = random.sample(expore_users,12)
    context = {'users':random_user}
    return render(request, 'ins/explore_people.html', context)

def explore(request):
    articles = InsArticle.objects.all().order_by('-pub_time')
    pagenator = Paginator(articles, 24)

    context = {'page': pagenator.page(1)}

    return render(request, 'ins/explore.html', context)


@csrf_exempt
def signin(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    print (name,password)
    if '@' in name:
        try:
            user = InsUser.objects.get(email=name)
        except:
            user = None
    else:
        try:
            user = InsUser.objects.get(username=name)
        except:
            user = None
    if not user:
        return JsonResponse({'false':'用户名或邮箱错误'})
    truepwd = user.password
    if password != truepwd:
        return  JsonResponse({'false':'密码错误'})
    request.session['islogin'] = True
    response = render(request,'ins/login.html')
    response.set_cookie('islogin','true',3600)
    return response

@csrf_exempt
def signup(request):
    phone_email = request.POST.get('phone_email')
    full_name = request.POST.get('full_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    print phone_email,full_name,username,password
    if phone_email and full_name and username and password:
        user = InsUser()
        user.username = username
        user.full_name = full_name
        user.password = password
        if '@' in phone_email:
            user.email = phone_email
        else:
            user.phone = phone_email
        try:
            user.save()
        except:
            return JsonResponse({'false':'fail to regi'})
    return JsonResponse({'true': '注册成功'})

def login_quit(request):
    print 'haha' * 100
    response = JsonResponse({'true':''})
    return response