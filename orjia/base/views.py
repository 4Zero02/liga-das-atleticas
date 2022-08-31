from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    template = 'base/content.html'
    return render(request, template)


# class SingUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'cadastro-atletica.html'


def logar(request):
    if request.user.is_authenticated:
        return redirect('base:index')
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = authenticate(username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('base:index')
            else:
                messages.error(request, 'Usuário inativo')
        else:
            messages.error(request, 'Usuário ou senha inválidos!')
    return render(request, 'base/login.html', locals())


@login_required
def sair(request):
    logout(request)
    return redirect('base:index')


# @login_required()
# def index(request):
#     return render(request, 'base/index.html', locals())