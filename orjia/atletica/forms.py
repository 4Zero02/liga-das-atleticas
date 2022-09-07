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
    error_messages = {
        'password_mismatch': 'The two password fields didnt match.',
    }
    password1 = forms.CharField(
        label="Senha", strip=False, widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg', 'placeholder': 'Senha'})
    )
    password2 = forms.CharField(
        label="Confirmar senha", strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'class': 'form-control form-control-lg',
                'placeholder': 'Confirmação de senha'
            }
        )
    )

    class Meta:
        model = Atletica
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'], code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        instance = super().save(False)
        user = User(username=self.cleaned_data["email"],email=self.cleaned_data["email"])
        user.set_password(self.cleaned_data["password1"])
        instance.usuario = user

        if commit:
            user.save()
            instance.save()
