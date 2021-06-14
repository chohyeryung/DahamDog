from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Application(models.Model):    #아마도 지원 테이블인듯하다! 유저를 만들고 만들어야할듯
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    commented = models.DateTimeField(auto_now_add=True)
