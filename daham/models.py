from django.db import models

class Board(models.Model):
    area = models.CharField(max_length=50)
    content = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    apply_count = models.IntegerField()

    def __str__(self):
        return f'{self.content} {self.posted}'

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    commented = models.DateTimeField(auto_now_add=True)
