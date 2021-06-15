from django import forms
from daham.models import Board, Comment


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']

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