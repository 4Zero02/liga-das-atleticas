from django import forms
from .models import Atletica, Atleta, Equipe
from base.models import User
from django.core.validators import MinValueValidator


class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['modalidade', 'atletica', 'campanha', 'atleta']
        # 'atleta' = forms.ModelMultipleChoiceField(queryset=Atleta.objects.all())
        widgets = {
            'modalidade': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
            'atletica': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
            'campanha': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
            # 'atleta': forms.widgets.SelectMultiple(
            #     attrs={'class': 'form-control form-control-lg text-center'}
            # ),
        }

        def __init__(self, *args, **kwargs):
            super(EquipeForm, self).__init__(*args, **kwargs)
            self.fields['atleta'] = forms.ModelMultipleChoiceField(
                widget=forms.widgets.SelectMultiple, queryset=Atleta.objects.all()
            )


class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ('nome', 'matricula', 'chave', 'atletica', 'naipe')
        widgets = {
            'naipe': forms.Select(
                attrs={'class': 'form-control form-control-lg text-center'}
            ),
            # 'atletica': forms.Select(
            #     attrs={'class': 'form-control form-control-lg text-center'}
            # ),
            'atletica': forms.HiddenInput(),
        }

    # def save(self, commit=True):
    #     instance = super().save(False)
    #     user = User(full_name=self.cleaned_data["nome"], email=self.cleaned_data["email"])
    #     user.set_password(self.cleaned_data["password1"])
    #
    #     if commit:
    #         user.save()
    #         instance.usuario = user
    #         instance.save()
    #
    #     return instance


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
        fields = ('nome', 'email', 'curso', 'instagram', 'twitter', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
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
        user = User(full_name=self.cleaned_data["nome"], email=self.cleaned_data["email"])
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            instance.usuario = user
            instance.save()

        return instance


class AtleticaChangeForm(forms.ModelForm):
    class Meta:
        model = Atletica
        fields = ('nome', 'email', 'curso', 'instagram', 'twitter')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
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
