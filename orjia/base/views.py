from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from .forms import AuthForm
from atletica.models import Atletica

User = get_user_model()


def home(request):
    template = 'base/content.html'
    atleticas = Atletica.objects.all()
    context = {'atleticas': atleticas}
    return render(request, template, context)


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm


# @login_required
class LogoutView(LogoutView):
    template_name = ''
