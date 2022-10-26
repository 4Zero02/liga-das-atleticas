from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PartidaForm, RankingForm
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
    return render(request, 'partida/partida_create.html', {'form': partida_form})
