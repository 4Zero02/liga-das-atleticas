from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AtletaForm
from .forms import AtleticaForm, AtleticaChangeForm
from .models import Atletica


@login_required()
def atleta_add(request):
    form = AtletaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('base:index')
    return render(request, 'atleta_form.html', {'form': form})


class AtleticaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'atletica/atletica_create.html'
    model = Atletica
    form_class = AtleticaForm
    success_message = '%(nome)s cadastrado com sucesso'
    success_url = reverse_lazy('atletica:atletica_detail')


class AtleticaList(LoginRequiredMixin, ListView):
    model = Atletica
    template = 'atletica/atletica_list.html'


class AtleticaDetail(LoginRequiredMixin, SuccessMessageMixin, DetailView):
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
