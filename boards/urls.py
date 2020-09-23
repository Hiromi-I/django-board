from django.urls import path

from .views import IndexView, CreateBoardView, UpdateBoardView, DeleteBoardView

app_name = "boards"

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("create/", CreateBoardView.as_view(), name='create'),
    path("update/<int:pk>/", UpdateBoardView.as_view(), name='update'),
    path("delete/<int:pk>/", DeleteBoardView.as_view(), name='delete'),
]
