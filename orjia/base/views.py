from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from .forms import AuthForm
from atletica.models import Atletica, Score, Equipe
from campanha.models import Campanha, Competicao
from partida.services.partidas_service import make_ranking

User = get_user_model()


def home(request):
    template = 'base/content.html'
    campanha = Campanha.objects.get(status=1)
    competicoes = Competicao.objects.filter(campanha=campanha)
    atleticas = Atletica.objects.all()
    # print('competicoes:')
    # print(competicoes)
    for atletica in atleticas:
        try:
            score = Score.objects.get(campanha=campanha, atletica=atletica)
            score.pontos = 0
            score.save()
        except Score.DoesNotExist:
            score = Score(campanha=campanha, atletica=atletica, pontos=0)
            score.save()
    for competicao in competicoes:
        equipes = Equipe.objects.filter(competicao=competicao)
        # print(competicao)
        # print(equipes)
        ranking = make_ranking(competicao)
        if ranking:
            pontos = 20
            for equipe in ranking:
                if equipe:
                    score = Score.objects.get(campanha=campanha, atletica=equipe.atletica)
                    score.pontos += pontos
                    score.save()
                    pontos -= 2
                    # print(equipe.atletica)
                    # print(score.pontos)
            for equipe in equipes:
                if equipe not in ranking:
                    score = Score.objects.get(campanha=campanha, atletica=equipe.atletica)
                    score.pontos += 1
                    score.save()
                    # print(equipe.atletica)
                    # print(score.pontos)
    score = Score.objects.all().order_by('-pontos')
    context = {'score': score, "campanha": campanha}
    return render(request, template, context)


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm


# @login_required
class LogoutView(LogoutView):
    template_name = ''
