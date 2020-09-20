from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import BoardCreationForm
from .models import Board


class IndexView(LoginRequiredMixin, ListView):
    model = Board
    context_object_name = "boards"
    template_name = "boards/index.html"


class CreateBoardView(CreateView):
    form_class = BoardCreationForm
    template_name = "boards/create.html"
    success_url = reverse_lazy('boards:index')
