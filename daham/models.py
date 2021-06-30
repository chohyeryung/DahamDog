from django.contrib.auth.models import User
from django.conf import settings
from django.db import models


# 유저와 1:1 연결, 이미지, 한줄소개 저장하기 위해
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 1:1로 연결
    nickname = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)


class Board(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to="images/", null=True)
    end_date = models.DateField(null=True)  #봉사 날짜
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Application(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # 유저
    created_date = models.DateTimeField(auto_now_add=True)
