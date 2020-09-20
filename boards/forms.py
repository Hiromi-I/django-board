from django.forms import ModelForm

from .models import Board


class BoardCreationForm(ModelForm):
    class Meta:
        model = Board
        fields = ('name', 'description')
