from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AtletaForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AtleticaForm
from .models import Atletica


@login_required()
def atleta_add(request):
    form = AtletaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('base:index')
    return render(request, 'atleta_form.html', {'form': form})


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'forms/atletica_form.html'
    model = Atletica
    form_class = AtleticaForm
    success_message = '%(nome)s cadastrado com sucesso'
    success_url = reverse_lazy('base:index')
