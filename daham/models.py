from django.db import models


# class User(models.Model): 유저 모델
#     name = models.CharField(max_length=200, verbose_name='이름')
#     email = models.EmailField(max_length=128, verbose_name='이메일')
#     password = models.CharField(max_length=64, verbose_name='비밀번호')


class Board(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    title = models.CharField(max_length=200, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Application(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  #유저
    created_date = models.DateTimeField(auto_now_add=True)