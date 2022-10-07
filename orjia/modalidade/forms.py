from .models import Modalidade
from django import forms


class ModalidadeForm(forms.ModelForm):

    class Meta:
        model = Modalidade
        fields = ('nome', 'tipo', 'max_atletas', 'min_atletas', 'tipo_confronto')
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome da modalidade'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
            'max_atletas': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Maximo de atletas'}
            ),
            'min_atletas': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Minimo de atletas'}
            ),
            'tipo_confronto': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
        }
