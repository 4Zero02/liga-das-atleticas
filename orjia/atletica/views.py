from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AtleticaForm, AtleticaChangeForm, EquipeForm, AtletaForm, AtletaUpdateForm
from .models import Atletica, Atleta, Equipe


class AtletaList(LoginRequiredMixin, ListView):
    model = Atleta
    template_name: str = 'atleta/atleta_list.html'


def atleta_list(request):
    template_name = 'atleta/atleta_list.html'
    atletica_id = Atletica.objects.get(usuario=request.user)
    atleta_list = Atleta.objects.filter(atletica=atletica_id).order_by('nome')
    context = {'atletas': atleta_list}
    return render(request, template_name, context)


@login_required
def atleta_add(request):
    form = AtletaForm(request.POST or None)
    atletica_id = Atletica.objects.get(usuario=request.user)
    if form.is_valid():
        form = form.save(commit=False)
        form.atletica = atletica_id
        form.save()
        return redirect('atletica:atleta_list')
    return render(request, 'atleta/atleta_create.html', {'form': form})


class AtletaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Atleta
    form_class = AtletaUpdateForm
    template_name: str = 'atleta/atleta_update.html'
    # success_message = "Atleta %(nome)s atualizado com sucesso!"
    success_url = reverse_lazy('atletica:atleta_list')


def atleta_delete(request, pk):
    atleta = Atleta.objects.get(pk=pk)
    form = AtletaForm(instance=atleta)
    if request.method == 'POST':
        atleta.delete()
        return redirect('atletica:atleta_list')


class AtleticaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'atletica/atletica_create.html'
    model = Atletica
    form_class = AtleticaForm
    success_message = '%(nome)s cadastrado com sucesso'
    # success_url = reverse_lazy('atletica:atletica_detail')

    def get_success_url(self):
        return reverse_lazy(
            'atletica:atletica_detail', kwargs={"pk": self.object.pk}
        )


class AtleticaDelete(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    model = Atletica
    success_url = reverse_lazy('atletica:atletica_list')


class EquipeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'equipe/equipe_create.html'
    model = Equipe
    form_class = EquipeForm
    # success_message = '%(nome)s cadastrado com sucesso'
    success_url = reverse_lazy('atletica:atleta_list')



class AtleticaList(ListView):
    model = Atletica
    template = 'atletica/atletica_list.html'


class AtleticaDetail(SuccessMessageMixin, DetailView):
    model = Atletica
    template_name: str = 'atletica/atletica_detail.html'


class AtleticaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Atletica
    form_class = AtleticaChangeForm
    template_name: str = 'atletica/atletica_update.html'
    success_message = "Atlética %(nome)s atualizada com sucesso!"

    def get_success_url(self):
        return reverse_lazy(
            'atletica:atletica_detail', kwargs={"pk": self.object.pk}
        )
