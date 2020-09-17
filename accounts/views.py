from django.contrib.auth import views, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


class LoginView(views.LoginView):
    template_name = "accounts/login.html"


class LogoutView(views.LogoutView):
    pass


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('boards:index')
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid
