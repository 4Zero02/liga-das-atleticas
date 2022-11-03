from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from .forms import AuthForm
from atletica.models import Atletica, Score, Equipe
from campanha.models import Campanha, Competicao

User = get_user_model()


def home(request):
    template = 'base/content.html'
    campanha = Campanha.objects.get(status=1)
    competicoes = Competicao.objects.filter(campanha=campanha)
    atleticas = Atletica.objects.all()
    equipes = []
    print('competicoes:')
    print(competicoes)
    print('equipes/comp:')
    print(equipes)
    for atletica in atleticas:
        try:
            score = Score.objects.get(campanha=campanha, atletica=atletica)
            score.pontos = 0
            score.save()
            print(score)
        except Score.DoesNotExist:
            score = Score(campanha=campanha, atletica=atletica, pontos=0)
            score.save()
            print(score)
    for competicao in competicoes:
        equipes.append(Equipe.objects.filter(competicao=competicao))
    for equipe in equipes:
        for time in equipe:
            # verificar qual equipe ta no ranking
            # Chama a def ranking
            pass

    context = {'atleticas': atleticas}
    return render(request, template, context)


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm


# @login_required
class LogoutView(LogoutView):
    template_name = ''
