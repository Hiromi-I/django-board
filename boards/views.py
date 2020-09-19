from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Board


class IndexView(LoginRequiredMixin, ListView):
    model = Board
    context_object_name = "boards"
    template_name = "boards/index.html"
