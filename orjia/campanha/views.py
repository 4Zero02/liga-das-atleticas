from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Campanha, Competicao
from .forms import CampanhaForm, CompeticaoForm, CompeticaoUpdateForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from partida.models import Partida, Ranking, Competidor
from partida.forms import RankingForm


class CampanhaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "campanha/campanha_create.html"
    model = Campanha
    form_class = CampanhaForm
    success_message = "Campanha %(nome)s cadastrada com sucesso"

    # success_url = reverse_lazy('atletica:atletica_detail')

    def get_success_url(self):
        return reverse_lazy("campanha:campanha_detail", kwargs={"pk": self.object.pk})


@login_required
def competicao_create(request):
    form = CompeticaoForm(request.POST or None)
    campanha = Campanha.objects.get(status=1)
    if form.is_valid():
        form = form.save(commit=False)
        form.campanha = campanha
        form.save()
        return redirect("campanha:campanha_detail", campanha.pk)
    return render(
        request,
        "competicao/competicao_create.html",
        {"form": form, "campanha": campanha},
    )


class CompeticaoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Competicao
    form_class = CompeticaoUpdateForm
    template_name: str = "competicao/competicao_update.html"
    success_message = "Competição atualizada com sucesso!"

    def get_success_url(self):
        return reverse_lazy(
            "campanha:campanha_detail", kwargs={"pk": self.object.campanha.id}
        )


class CampanhaDetail(SuccessMessageMixin, DetailView):
    model = Campanha
    template_name: str = "campanha/campanha_detail.html"


def campanha_detail(request, pk):
    template_name = "campanha/campanha_detail.html"
    campanha = Campanha.objects.get(pk=pk)
    competicao = Competicao.objects.filter(campanha=campanha)
    context = {"campanha": campanha, "competicao": competicao}
    return render(request, template_name, context)


def competicao_detail(request, pk):
    template_name = "competicao/competicao_detail.html"
    competicao = Competicao.objects.get(pk=pk)
    competidores = Partida.equipes.through.objects.filter(
        partida__competicao=competicao
    )

    # Monta uma lista L onde cada elemento é outra lista Lx, com 2 partida_competidores
    # Lx[i] é a equipe A da partida X e Lx[i + 1] é a equipe B da partida X
    partida_competidor = [
        [competidores[i], competidores[i + 1]] for i in range(0, len(competidores), 2)
    ]

    # Busca as partida_competidores que estão nas etapas Final e TerceiroLugar
    # para a competição X
    partida_ranking = competidores.filter(
        partida__etapa__in=[Partida.Etapa.FINAL, Partida.Etapa.TERCEIRO]
    ).prefetch_related("equipe")

    result_ranking = []

    # Itera sobre as partida_competidores que estão na Final e TerceiroLugar
    # O loop vai de 2 em 2, pois cada partida tem 2 equipes
    # O primeiro loop é da final e o segundo é para TerceiroLugar
    for idx in range(0, len(partida_ranking), 2):
        if partida_ranking[idx].resultado > partida_ranking[idx + 1].resultado:
            result_ranking.extend(
                [partida_ranking[idx].equipe, partida_ranking[idx + 1].equipe]
            )
        else:
            result_ranking.extend(
                [partida_ranking[idx + 1].equipe, partida_ranking[idx].equipe]
            )

    context = {
        "competicao": competicao,
        "competidores": partida_competidor,
        "ranking": result_ranking,
    }
    return render(request, template_name, context)


class CampanhaList(ListView):
    model = Campanha
    template = "campanha/campanha_list.html"


class CampanhaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Campanha
    form_class = CampanhaForm
    template_name: str = "campanha/campanha_update.html"
    success_message = "Campanha %(nome)s atualizada com sucesso!"

    def get_success_url(self):
        return reverse_lazy("campanha:campanha_detail", kwargs={"pk": self.object.pk})


def ranking(request, pk):
    template_name = "ranking/ranking.html"
    competicao = Competicao.objects.get(pk=pk)
    # competidores = Partida.equipes.through.objects.filter(partida__competicao=competicao)
    partidas = Partida.objects.filter(
        competicao=competicao, etapa__in=["FINAL", "TERCEIRO"]
    )
    competidores = partidas.equipes.all()
    print(competidores)

    context = {"result": competidores}
    return render(request, template_name, context)
