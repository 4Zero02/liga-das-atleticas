from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Campanha, Competicao
from .forms import CampanhaForm, CompeticaoForm, CompeticaoUpdateForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from partida.models import Partida, Ranking


class CampanhaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'campanha/campanha_create.html'
    model = Campanha
    form_class = CampanhaForm
    success_message = 'Campanha %(nome)s cadastrada com sucesso'
    # success_url = reverse_lazy('atletica:atletica_detail')

    def get_success_url(self):
        return reverse_lazy(
            'campanha:campanha_detail', kwargs={"pk": self.object.pk}
        )


@login_required
def competicao_create(request):
    form = CompeticaoForm(request.POST or None)
    campanha = Campanha.objects.get(status=1)
    if form.is_valid():
        form = form.save(commit=False)
        form.campanha = campanha
        form.save()
        return redirect('campanha:campanha_detail', campanha.pk)
    return render(request, 'competicao/competicao_create.html', {'form': form})


class CompeticaoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Competicao
    form_class = CompeticaoUpdateForm
    template_name: str = 'competicao/competicao_update.html'
    success_message = "Competição atualizada com sucesso!"

    def get_success_url(self):
        return reverse_lazy(
            'campanha:campanha_detail', kwargs={"pk": self.object.campanha.id}
        )


class CampanhaDetail(SuccessMessageMixin, DetailView):
    model = Campanha
    template_name: str = 'campanha/campanha_detail.html'


def campanha_detail(request, pk):
    template_name = 'campanha/campanha_detail.html'
    campanha = Campanha.objects.get(pk=pk)
    competicao = Competicao.objects.filter(campanha=campanha)
    context = {'campanha': campanha, 'competicao': competicao}
    return render(request, template_name, context)


def competicao_detail(request, pk):
    template_name = 'competicao/competicao_detail.html'
    competicao = Competicao.objects.get(pk=pk)
    partida = Partida.objects.filter(competicao=competicao)
    ranking = Ranking.objects.get(competicao=competicao)
    context = {'competicao': competicao, 'partida': partida}
    return render(request, template_name, context)


class CampanhaList(ListView):
    model = Campanha
    template = 'campanha/campanha_list.html'


class CampanhaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Campanha
    form_class = CampanhaForm
    template_name: str = 'campanha/campanha_update.html'
    success_message = "Campanha %(nome)s atualizada com sucesso!"

    def get_success_url(self):
        return reverse_lazy(
            'campanha:campanha_detail', kwargs={"pk": self.object.pk}
        )
