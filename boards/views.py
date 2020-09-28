from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import resolve_url, get_object_or_404

from .forms import BoardCreationForm, CommentCreationForm
from .models import Board, Comment


class IndexView(LoginRequiredMixin, ListView):
    model = Board
    context_object_name = "boards"
    template_name = "boards/index.html"


class CreateBoardView(CreateView):
    form_class = BoardCreationForm
    template_name = "boards/create.html"
    success_url = reverse_lazy('boards:index')


class UpdateBoardView(UpdateView):
    model = Board
    form_class = BoardCreationForm
    template_name = "boards/update.html"
    success_url = reverse_lazy('boards:index')


class DeleteBoardView(DeleteView):
    model = Board
    success_url = reverse_lazy('boards:index')


class BoardDetailView(CreateView):
    form_class = CommentCreationForm
    template_name = "boards/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        board_id = self.kwargs.get("pk")
        context["board"] = get_object_or_404(Board, pk=board_id)
        context["comments"] = Comment.objects.filter(board__id=board_id)
        return context

    def form_valid(self, form):
        board_id = self.kwargs.get("pk")
        form.instance.user = self.request.user
        form.instance.board = get_object_or_404(Board, pk=board_id)
        return super().form_valid(form)

    def get_success_url(self):
        board_id = self.kwargs.get("pk")
        return resolve_url('boards:detail', pk=board_id)
