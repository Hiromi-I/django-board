from django.forms import ModelForm

from .models import Board, Comment


class BoardCreationForm(ModelForm):
    class Meta:
        model = Board
        fields = ('name', 'description')


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
