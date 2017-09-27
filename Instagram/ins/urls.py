#coding=utf-8
from django.conf.urls import url
from ins import views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'index',views.index),
    url(r'blog',views.blog),
    url(r'login',views.login),
    url(r'home',views.home),
    url(r'account/edit',views.edit),
    url(r'account/chpass',views.chpass),
    url(r'account/manage_access',views.manage_access),
    url(r'account/comment_filter',views.comment_filter),
    url(r'account/email_set',views.email_set),
    url(r'account/contact_history',views.contact_history),
    url(r'explore/people',views.explore_people),

]
