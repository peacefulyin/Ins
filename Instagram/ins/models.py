from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    phone = models.IntegerField(null=True)
    eamil = models.EmailField(null=True)
    about_self = models.CharField(max_length=1000)
    gender = models.IntegerField(default=3)
    is_private = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)


class Friend(models.Model):
    people = models.ForeignKey(User, related_name='firend_people')
    target = models.ForeignKey(User, related_name='firend_target')

class Block(models.Model):
    people = models.ForeignKey(User, related_name='block_people')
    target = models.ForeignKey(User, related_name='block_target')


class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100,null=True)
    text = models.TextField()
    pub_time = models.DateTimeField()

class Comment(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=1000)
    pub_time = models.DateTimeField()



