from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PartidaForm, RankingForm, PartidaUpdateForm, ResultadoForm
#CompetidorForm
from .models import Partida, Ranking, Competidor
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


def partida_detail(request, pk):
    partida = Partida.objects.get(pk=pk)
    competidor_partida = Competidor.objects.filter(partida=partida)
    print(competidor_partida)
    context = {'partida': partida, 'competidor': competidor_partida}
    return render(request, 'partida/partida_detail.html', context)
    # pass


def resultado_create(request, pk):
    partida = Partida.objects.get(pk=pk)
    template_name = 'competidor/resultado_add.html'
    competior_form = Competidor()
    competidor_resultado_formset = inlineformset_factory(
        Partida,
        Competidor,
        form=ResultadoForm,
        extra=0,
        min_num=2,
        validate_min=True,
    )
    if request.method == 'POST':
        formset = competidor_resultado_formset(
            request.POST,
            instance=competior_form,
            prefix=partida
        )
        print('form:')
        print(formset)
        if formset.is_valid():
            formset.save()
            # url = 'estoque:estoque_entrada_detail'
            # return HttpResponseRedirect(resolve_url(url, .pk))
    else:
        formset = competidor_resultado_formset(instance=competior_form, prefix=partida)

    context = {'formset': formset, 'partida': partida}
    return render(request, template_name, context)
