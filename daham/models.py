from django.contrib.auth.models import User
from django.db import models

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    title = models.CharField(max_length=200, null=True)
    content = models.TextField()
    end_date = models.DateField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(null=True, blank=True)


class Application(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    created_date = models.DateTimeField(auto_now_add=True)