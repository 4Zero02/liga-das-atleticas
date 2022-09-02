from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AtletaForm
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


@login_required()
def atleta_add(request):
    form = AtletaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('base:index')
    return render(request, 'atleta_form.html', {'form': form})

# class SingUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'cadastro-atletica.html'


def atletica_add(request):
    pass