from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from .forms import AuthForm
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    template = 'base/content.html'
    return render(request, template)


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm


# @login_required
class LogoutView(LogoutView):
    template_name = ''


@login_required()
def atletica_add(request):
    return render(request, 'dashboard.html', locals())
