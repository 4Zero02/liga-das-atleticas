from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import (
    AtleticaForm,
    AtleticaChangeForm,
    EquipeForm,
    EquipeUpdateForm,
    AtletaForm,
    AtletaUpdateForm,
)
from .models import Atletica, Atleta, Equipe
from campanha.models import Campanha, Competicao
from django.db.models import Q


def equipe_list(request):
    template_name = "equipe/equipe_list.html"
    atletica_id = Atletica.objects.get(usuario=request.user)
    equipe_list = Equipe.objects.filter(atletica=atletica_id)
    equipe_masc = Equipe.objects.filter(atletica=atletica_id, sex="M")
    equipe_fem = Equipe.objects.filter(atletica=atletica_id, sex="F")
    context = {
        "object_list": equipe_list,
        "object_masc": equipe_masc,
        "object_fem": equipe_fem,
    }
    return render(request, template_name, context)


@login_required
def equipe_create(request):
    atletica = Atletica.objects.get(usuario=request.user)
    campanha = Campanha.objects.get(status=1)

    equipe_form = EquipeForm(request.POST or None, atletica=atletica)

    if request.method == "POST":
        if equipe_form.is_valid():
            form = equipe_form.save(commit=False)
            form.campanha = campanha
            form.atletica = atletica
            sex = form.competicao.sex
            form.sex = sex
            form.save()
            equipe_form.save_m2m()
            return redirect("atletica:equipe_list")

    return render(request, "equipe/equipe_create.html", {"form": equipe_form})


@login_required
def equipe_delete(request, pk):
    equipe = Equipe.objects.get(pk=pk)
    form = EquipeForm(instance=equipe)
    if request.method == "POST":
        equipe.delete()
        return redirect("atletica:equipe_list")


class EquipeUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Equipe
    form_class = EquipeUpdateForm
    template_name: str = "equipe/equipe_create.html"
    # success_message = "Atleta %(nome)s atualizado com sucesso!"
    success_url = reverse_lazy("atletica:equipe_list")


def atleta_list(request):
    template_name = "atleta/atleta_list.html"
    atletica_id = Atletica.objects.get(usuario=request.user)
    atleta_list = Atleta.objects.filter(atletica=atletica_id).order_by("nome")
    context = {"atletas": atleta_list, "atletica": atletica_id}
    return render(request, template_name, context)


@login_required
def atleta_add(request):
    form = AtletaForm(request.POST or None)
    atletica_id = Atletica.objects.get(usuario=request.user)
    if form.is_valid():
        form = form.save(commit=False)
        form.atletica = atletica_id
        form.save()
        return redirect("atletica:atleta_list")
    return render(request, "atleta/atleta_create.html", {"form": form})


class AtletaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Atleta
    form_class = AtletaUpdateForm
    template_name: str = "atleta/atleta_update.html"
    # success_message = "Atleta %(nome)s atualizado com sucesso!"
    success_url = reverse_lazy("atletica:atleta_list")


def atleta_delete(request, pk):
    atleta = Atleta.objects.get(pk=pk)
    form = AtletaForm(instance=atleta)
    if request.method == "POST":
        atleta.delete()
        return redirect("atletica:atleta_list")


class AtleticaCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "atletica/atletica_create.html"
    model = Atletica
    form_class = AtleticaForm
    success_message = "Atletica %(nome)s cadastrada com sucesso"

    # success_url = reverse_lazy('atletica:atletica_detail')

    def get_success_url(self):
        return reverse_lazy("atletica:atletica_detail", kwargs={"pk": self.object.pk})


class AtleticaList(ListView):
    model = Atletica
    template = "atletica/atletica_list.html"


class AtleticaDetail(SuccessMessageMixin, DetailView):
    model = Atletica
    template_name: str = "atletica/atletica_detail.html"


class AtleticaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Atletica
    form_class = AtleticaChangeForm
    template_name: str = "atletica/atletica_update.html"
    success_message = "Atlética %(nome)s atualizada com sucesso!"

    def get_success_url(self):
        return reverse_lazy("atletica:atletica_detail", kwargs={"pk": self.object.pk})


class AtleticaDelete(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    model = Atletica
    success_url = reverse_lazy("atletica:atletica_list")
