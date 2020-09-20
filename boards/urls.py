from django.urls import path

from .views import IndexView, CreateBoardView

app_name = "boards"

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("create/", CreateBoardView.as_view(), name='create'),
]
