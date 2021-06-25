from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.db import models

from daham.models import Board, Comment, Profile


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'end_date']

        # labels = {
        #     'title': '제목',
        #     'content': '내용',
        # }

        # widgets = {
        #     'title': forms.TextInput(attrs={'placeholder': '제목'}),
        #     'content': forms.Textarea(attrs={'placeholder': '내용'}),
        # }

        # widgets = {
        #     'title': forms.TextInput(attrs={'placeholder': 'Name'}),
        #     'content': forms.Textarea(
        #         attrs={'placeholder': 'Enter description here'}),
        # }


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