from asyncio import base_events
from dataclasses import fields
from email.mime import base
from xml.dom import ValidationErr
from django import forms
from django.forms import modelformset_factory, BaseModelFormSet
from .models import Ranking, Partida, Competidor
from atletica.models import Equipe


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        super().__init__(format="%Y-%m-%d", attrs={"class": "form-control"})


class RankingForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ()


class PartidaForm(forms.ModelForm):
    equipes = forms.ModelMultipleChoiceField(
        label="Equipes",
        required=True,
        queryset=Equipe.objects.none(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control form-control-lg text-center js-example-basic-multiple",
                "multiple": "multiple",
            }
        ),
    )

    class Meta:
        model = Partida
        fields = ("competicao", "numero", "data", "local", "equipes", "etapa", "md")
        widgets = {
            "competicao": forms.HiddenInput(),
            "local": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Nome do atleta",
                }
            ),
            "numero": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Sequencia do jogo",
                }
            ),
            "data": DateInput(),
            "etapa": forms.Select(
                attrs={"class": "form-control form-control-lg", "placeholder": "Etapa"}
            ),
            "md": forms.Select(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Melhor de...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        competicao = kwargs.pop("competicao", None)

        super(PartidaForm, self).__init__(*args, **kwargs)

        if competicao:
            base_qs = Equipe.objects.filter(competicao=competicao)

            if competicao.sex != "O":
                base_qs = base_qs.filter(sex=competicao.sex)

            self.fields["equipes"].queryset = base_qs


class PartidaUpdateForm(forms.ModelForm):
    equipes = forms.ModelMultipleChoiceField(
        label="Equipes",
        required=True,
        queryset=Equipe.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control form-control-lg text-center js-example-basic-multiple",
                "multiple": "multiple",
            }
        ),
    )

    class Meta:
        model = Partida
        fields = ("numero", "data", "local", "equipes", "etapa", "md")
        widgets = {
            "local": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Nome do atleta",
                }
            ),
            "numero": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Sequencia do jogo",
                }
            ),
            "data": DateInput(),
            "etapa": forms.Select(
                attrs={"class": "form-control form-control-lg", "placeholder": "Etapa"}
            ),
            "md": forms.Select(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Melhor de...",
                }
            ),
        }


class ResultadoForm(forms.ModelForm):
    class Meta:
        model = Competidor
        fields = ("resultado", "qualificador")
        widgets = {
            "resultado": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Resultado da Equipe",
                }
            ),
            "qualificador": forms.TextInput(
                attrs={"class": "form-control form-control-lg"}
            ),
        }


class CompetidorResultadoUpdateForm(forms.ModelForm):
    equipe_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Equipe",
                "readonly": "true",
            }
        ),
    )

    class Meta:
        model = Competidor
        fields = ("equipe", "equipe_name", "resultado")
        widgets = {
            "equipe": forms.HiddenInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "readonly": "true",
                }
            ),
            "resultado": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Resultado",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        competidor = kwargs.get("instance", None)

        super(CompetidorResultadoUpdateForm, self).__init__(*args, **kwargs)

        if competidor:
            self.fields["equipe_name"].initial = competidor.equipe.atletica

    def clean_equipe(self):
        equipe = self.cleaned_data["equipe"]
        try:
            return Equipe.objects.get(pk=equipe.pk)
        except Equipe.DoesNotExist:
            raise ValidationErr("Equipe não existe!")


CompetidorResultadoUpdateFormSet = modelformset_factory(
    Competidor, form=CompetidorResultadoUpdateForm, extra=0
)
