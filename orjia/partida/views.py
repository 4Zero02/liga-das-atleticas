from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PartidaForm, RankingForm, PartidaUpdateForm
from .models import Partida, Ranking
from campanha.models import Competicao


@login_required
def partida_create(request, pk):
    partida_form = PartidaForm(request.POST or None)
    competicao = Competicao.objects.get(pk=pk)
    if partida_form.is_valid():
        form = partida_form.save(commit=False)
        form.competicao = competicao
        form.save()
        partida_form.save_m2m()
        return redirect('campanha:competicao_detail', pk)
    return render(request, 'partida/partida_create.html', {'competicao': competicao, 'form': partida_form})


class PartidaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Partida
    form_class = PartidaUpdateForm
    template_name: str = 'partida/partida_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PartidaUpdate, self).get_context_data(*args, **kwargs)
        context['competicao'] = Competicao.objects.get(pk=self.object.competicao.pk)
        return context

    def get_success_url(self):
        return reverse_lazy(
            'campanha:competicao_detail', kwargs={"pk": self.object.competicao.pk}
        )


def partida_update(request, pk):
    partida_form = PartidaForm(request.POST or None)
    pass
