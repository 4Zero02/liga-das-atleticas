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
    class Meta:
        model = Partida
        fields = ('competicao', 'numero', 'data', 'equipeA', 'equipeB', 'equipe_vencedora', 'etapa')
        widgets = {
            'competicao': forms.HiddenInput(),
            'numero': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Sequencia do jogo'}),
            'data': DateInput(),
            'equipeA': forms.Select(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Equipe A'}),
            'equipeB': forms.Select(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Equipe B'}),
            'equipe_vencedora': forms.Select(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Equipe vencedora'}),
            'etapa': forms.Select(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Etapa'})
        }
