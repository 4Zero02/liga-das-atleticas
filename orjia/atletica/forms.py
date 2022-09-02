from django import forms
from .models import Atletica, Atleta
from django.contrib.auth.models import User
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

    def save(self, commit=True):
        user = User(email=self.cleaned_data["email"])
        user.set_password(self.cleaned_data["password"])
        instance = super().save(False)
        instance.usuario = user

        if commit:
            instance.save()