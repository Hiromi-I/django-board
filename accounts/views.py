from django.contrib.auth import views


class LoginView(views.LoginView):
    template_name = "accounts/login.html"


class LogoutView(views.LogoutView):
    pass
