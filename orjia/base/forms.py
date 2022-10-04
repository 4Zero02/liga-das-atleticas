from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Competicao, Campanha

User = get_user_model()


class CampanhaForm(forms.ModelForm):

    class Meta:
        model = Campanha
        fields = ('nome', 'data_inicio', 'data_final', 'ano', 'status')


class CompeticaoForm(forms.ModelForm):

    class Meta:
        model = Competicao
        fields = ('modalidade', 'data')
        widgets = {
            'modalidade': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
            'nome': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome completo'}
            ),
            'curso': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Curso que a atlética pertence'}
            ),
            'instagram': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Link da instagram da atlética'}
            ),
            'twitter': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'Link do Twitter da atlética'}
            )
        }


class AuthForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'autofocus': True, 'class': 'form-control form-control-lg', 'placeholder': 'Digite seu email'}
        )
    )
    password = forms.CharField(
        label=_("Password"), strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control form-control-lg',
                'placeholder': 'Senha'
            }
        )
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user = authenticate(self.request, username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(
                    _('Usuário ou senha inválido')
                )
                messages.add_message(self.request, messages.INFO, 'Hello world.')
            else:
                print("AAAAAAAAAAA")

        return self.cleaned_data

    def get_user(self):
        return self.user
