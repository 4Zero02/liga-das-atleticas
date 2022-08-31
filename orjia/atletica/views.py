from django.shortcuts import render, redirect
from .forms import AtletaForm

#login required
def atleta_add(request):
    form = AtletaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('base:index')
    return render(request, 'atleta_form.html', {'form': form})
