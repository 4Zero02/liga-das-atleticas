from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import (
    PartidaForm,
    RankingForm,
    PartidaUpdateForm,
    ResultadoForm,
    CompetidorResultadoUpdateForm,
    CompetidorResultadoUpdateFormSet,
)

# CompetidorForm
from .models import Partida, Ranking, Competidor
from campanha.models import Competicao


@login_required
def partida_create(request, pk):
    competicao = Competicao.objects.get(pk=pk)
    partida_form = PartidaForm(request.POST or None, competicao=competicao)

    if request.method == "POST":
        if partida_form.is_valid():
            form = partida_form.save(commit=False)
            form.competicao = competicao
            form.save()
            partida_form.save_m2m()
            return redirect("campanha:competicao_detail", pk)

    return render(
        request,
        "partida/partida_create.html",
        {"competicao": competicao, "form": partida_form},
    )


class PartidaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Partida
    form_class = PartidaUpdateForm
    template_name: str = "partida/partida_update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PartidaUpdate, self).get_context_data(*args, **kwargs)
        context["competicao"] = Competicao.objects.get(pk=self.object.competicao.pk)
        return context

    def get_success_url(self):
        return reverse_lazy(
            "campanha:competicao_detail", kwargs={"pk": self.object.competicao.pk}
        )


class CompeticaoResultadoUpdate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Competidor
    template_name = "competicao/gerenciar_resultado.html"
    form_class = CompetidorResultadoUpdateForm

    def get_context_data(self, **kwargs):
        context = super(CompeticaoResultadoUpdate, self).get_context_data(**kwargs)

        context["formset"] = CompetidorResultadoUpdateFormSet(
            queryset=Competidor.objects.filter(
                partida=self.kwargs["partida_pk"]
            ).prefetch_related("equipe")
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        formset = CompetidorResultadoUpdateFormSet(request.POST)
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            print(formset.errors)
            return self.form_invalid(formset)

    def get_success_url(self):
        competicao = Partida.objects.get(pk=self.kwargs["partida_pk"]).competicao
        return reverse_lazy("campanha:competicao_detail", kwargs={"pk": competicao.pk})


def partida_detail(request, pk):
    partida = Partida.objects.get(pk=pk)
    competidor_partida = Competidor.objects.filter(partida=partida)
    print(competidor_partida)
    context = {"partida": partida, "competidor": competidor_partida}
    return render(request, "partida/partida_detail.html", context)
    # pass
