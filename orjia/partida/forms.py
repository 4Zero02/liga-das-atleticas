from django import forms
from .models import Ranking, Partida
from atletica.models import Equipe


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        super().__init__(format='%Y-%m-%d', attrs={'class': 'form-control'})


class RankingForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ()


class PartidaForm(forms.ModelForm):
    equipes = forms.ModelMultipleChoiceField(
        label='Equipes',
        required=True,
        queryset=Equipe.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': 'form-control form-control-lg text-center js-example-basic-multiple',
                   'multiple': 'multiple'}
        )
    )

    class Meta:
        model = Partida
        fields = ('competicao', 'numero', 'data', 'local', 'equipes', 'etapa')
        widgets = {
            'competicao': forms.HiddenInput(),
            'local': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome do atleta'}
            ),
            'numero': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Sequencia do jogo'}),
            'data': DateInput(),
            'etapa': forms.Select(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Etapa'})
        }
