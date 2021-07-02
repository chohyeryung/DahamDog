from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from daham.models import Board, Comment, Profile


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'description', 'image']


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'image', 'end_date']

        widgets = {
            'end_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답글'
        }
