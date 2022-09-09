from .models import Modalidade
from django import forms


class ModalidadeForm(forms.ModelForm):

    class Meta:
        model = Modalidade
        fields = ('nome', 'tipo', 'max_atletas', 'min_atletas', 'naipe', 'tipo_confronto')
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome da modalidade'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
            'max_atletas': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Maximo de atletas permitido'}
            ),
            'min_atletas': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Minimo de atletas permitido'}
            ),
            'naipe': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
            'tipo_confronto': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
        }
