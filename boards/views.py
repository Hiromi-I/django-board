import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

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


class BoardDetailView(TemplateView):

    def _get_board(self, kwargs):
        board_id = kwargs.get("pk")
        return get_object_or_404(Board, pk=board_id)

    def get(self, request, **kwargs):
        board = self._get_board(kwargs)
        context = {
            "board": board,
            "comments": Comment.objects.filter(board=board).order_by('id'),
            "form": CommentCreationForm()
        }
        return render(request, "boards/detail.html", context)

    def post(self, request, **kwargs):
        board = self._get_board(kwargs)
        data = json.loads(request.body.decode('utf-8'))
        if data['body']:
            Comment.objects.create(
                body=data['body'], board=board, user=self.request.user)

        comments = Comment.objects.filter(board=board).order_by('id')
        comment_list = [{"id": comment.id,
                         "body": comment.body,
                         "user": comment.user.username}
                        for comment in comments]
        return JsonResponse(comment_list, safe=False)
