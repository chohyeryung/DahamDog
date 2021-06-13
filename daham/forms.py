from django import forms
from daham.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']