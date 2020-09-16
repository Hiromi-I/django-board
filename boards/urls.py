from django.urls import path

from .views import dummy

app_name = "boards"

urlpatterns = [
    path("", dummy),
]
