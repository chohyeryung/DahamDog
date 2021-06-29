from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.db import models

from daham.models import Board, Comment, Profile


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'image', 'end_date']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답글'
        }

# class CustomUserChangeForm(UserChangeForm):
#     password = None
#
#     class Meta:
#         model = get_user_model()
#         fields = ['email', 'username',]
#
#
# class ProfileForm(models.Model):
#     description = forms.CharField(label="한줄소개", required=False, widget=forms.Textarea())
#     image = forms.ImageField(label="프로필 이미지", required=False)
#
#     class Meta:
#         model = Profile
#         fields = ['description', 'image',]
