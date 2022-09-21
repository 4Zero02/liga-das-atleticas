from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from .forms import AuthForm
from base.models import Campanha, Competicao
from base.forms import CompeticaoForm, CampanhaForm

User = get_user_model()


def home(request):
    template = 'base/content.html'
    return render(request, template)


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm


# @login_required
class LogoutView(LogoutView):
    template_name = ''


def campanha_create(request):
    template_name = 'forms/competicao_form.html'
    campanha_form = Campanha()
    competicao_campanha_formset = inlineformset_factory(
        Campanha,
        Competicao,
        form=CompeticaoForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = CampanhaForm(
            request.POST, instance=campanha_form, prefix='campanha')
        formset = competicao_campanha_formset(
            request.POST,
            instance=campanha_form,
            prefix='competicao'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            # form.funcionario = request.user
            form.status = 1
            form.save()
            formset.save()
            url = 'base:index'
            return HttpResponseRedirect(resolve_url(url))
    else:
        form = CampanhaForm(instance=campanha_form, prefix='main')
        formset = competicao_campanha_formset(instance=campanha_form, prefix='competicao')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)
