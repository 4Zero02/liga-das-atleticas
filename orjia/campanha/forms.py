from django import forms
from .models import Campanha, Competicao


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        super().__init__(format='%Y-%m-%d', attrs={'class': 'form-control'})


class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ('nome', 'data_inicio', 'data_final', 'ano')
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome da campanha'}
            ),
            'ano': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Ano da campanha'}
            ),
            'data_inicio': DateInput(),
            'data_final': DateInput()
        }


class CompeticaoForm(forms.ModelForm):
    class Meta:
        model = Competicao
        fields = ('modalidade', 'data')
        widgets = {
            'modalidade': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
            'nome': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome completo'}
            ),
        }