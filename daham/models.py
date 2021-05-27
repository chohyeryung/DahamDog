from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=200, null=True)
    contents = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    contents = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Application(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    commented = models.DateTimeField(auto_now_add=True)
