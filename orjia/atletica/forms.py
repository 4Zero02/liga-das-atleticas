from django import forms
from .models import Atletica, Atleta
from django.core.validators import MinValueValidator


class AtletaForm(forms.ModelForm):

    class Meta:
        model = Atleta
        fields = '__all__'
        widgets = {
            'atletica': forms.HiddenInput(),
        }


class AtleticaForm(forms.ModelForm):

    class Meta:
        model = Atletica
        fields = '__all__'
