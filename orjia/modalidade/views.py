from django.shortcuts import render, redirect
from .forms import ModalidadeForm
from .models import Modalidade


def modalidade_add(request):
    form = ModalidadeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('modalidade:modalidade_list')
    return render(request, 'forms/modalidade_form.html', {'form': form})


def modalidade_list(request):
    modalidade = Modalidade.objects.all()
    template = 'modalidade/modalidade_list.html'
    return render(request, template, {'modalidades': modalidade})
    # pass
