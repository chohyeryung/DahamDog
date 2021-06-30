from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from daham.models import Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    nickname = forms.CharField(label='닉네임')

    class Meta:
        model = User
        fields = ("username", "email")

    def save(self):
        user = super().save()
        new_profile = Profile.objects.create(
            user=user,
            nickname=self.cleaned_data.get('nickname'),  # self.cleaned_data['nickname']
        )
        return new_profile


# class LoginForm(forms.ModelForm):
#     password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']
