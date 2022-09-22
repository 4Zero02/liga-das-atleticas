from django.shortcuts import render, redirect
from .forms import ModalidadeForm
from .models import Modalidade
from django.views.generic import UpdateView, DeleteView, DetailView


def modalidade_add(request):
    form = ModalidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('modalidade:modalidade_list')
    return render(request, 'modalidade/modalidade_create.html', {'form': form})


def modalidade_list(request):
    modalidade = Modalidade.objects.all()
    template = 'modalidade/modalidade_list.html'
    return render(request, template, {'modalidades': modalidade})


class ModalidadeUpdate(UpdateView):
    model = Modalidade
    template_name = 'modalidade/modalidade_edit.html'
    form_class = ModalidadeForm


def modalidade_delete(request, pk):
    modalidade = Modalidade.objects.get(pk=pk)
    form = ModalidadeForm(instance=modalidade)
    if request.method == 'POST':
        modalidade.delete()
        return redirect('modalidade:modalidade_list')
