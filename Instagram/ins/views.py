from django.shortcuts import render



def index(request):
    return render(request, 'ins/index.html')


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
    return render(request, 'ins/explore_people.html')

