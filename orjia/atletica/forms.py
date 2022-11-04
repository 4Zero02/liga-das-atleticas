from django import forms
from .models import Atletica, Atleta, Equipe
from base.models import User
from django.core.validators import MinValueValidator


# FORMS EQUIPE
class EquipeForm(forms.ModelForm):
    atleta = forms.ModelMultipleChoiceField(
        label="Atleta",
        required=True,
        queryset=Atleta.objects.none(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control form-control-lg text-center js-example-basic-multiple",
                "multiple": "multiple",
            }
        ),
    )

    class Meta:
        model = Equipe
        fields = ("competicao", "campanha", "atletica", "atleta", "sex")
        widgets = {
            "competicao": forms.Select(
                attrs={"class": "form-control form-control-lg text-center"}
            ),
            "atletica": forms.HiddenInput(),
            "sex": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        atletica = kwargs.pop("atletica", None)

        super(EquipeForm, self).__init__(*args, **kwargs)

        if atletica:
            self.fields["atleta"].queryset = Atleta.objects.filter(atletica=atletica)


class EquipeUpdateForm(forms.ModelForm):
    atleta = forms.ModelMultipleChoiceField(
        label="Atleta",
        required=True,
        queryset=Atleta.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control form-control-lg text-center js-example-basic-multiple",
                "multiple": "multiple",
            }
        ),
    )

    class Meta:
        model = Equipe
        fields = ("competicao", "atleta", "sex")
        widgets = {
            "competicao": forms.Select(
                attrs={"class": "form-control form-control-lg text-center"}
            ),
            "sex": forms.HiddenInput(),
        }


# FORMS ATLETA
class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ("nome", "matricula", "chave", "atletica", "sex")
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Nome do atleta",
                }
            ),
            "matricula": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Matricula do atleta",
                }
            ),
            "chave": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Chave de autenticacao",
                }
            ),
            "sex": forms.Select(
                attrs={"class": "form-control form-control-lg text-center"}
            ),
            "atletica": forms.HiddenInput(),
        }


class AtletaUpdateForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ("nome", "matricula", "chave", "sex")
        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Nome do atleta",
                }
            ),
            "matricula": forms.NumberInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Matricula do atleta",
                }
            ),
            "chave": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Chave de autenticacao",
                }
            ),
            "sex": forms.Select(
                attrs={"class": "form-control form-control-lg text-center"}
            ),
        }


# FORMS ATLETICA
class AtleticaForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": "The two password fields didnt match.",
    }
    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control form-control-lg",
                "placeholder": "Senha",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirmar senha",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control form-control-lg",
                "placeholder": "Confirmação de senha",
            }
        ),
    )
    logo = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "placeholder": "Foto",
                "accept": "image/jpeg,image/jpg,image/png",
            }
        ),
    )

    class Meta:
        model = Atletica
        fields = (
            "nome",
            "email",
            "curso",
            "instagram",
            "twitter",
            "password1",
            "password2",
            "logo",
        )
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control form-control-lg", "placeholder": "Email"}
            ),
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Nome completo",
                }
            ),
            "curso": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Curso que a atlética pertence",
                }
            ),
            "instagram": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Link da instagram da atlética",
                }
            ),
            "twitter": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Link do Twitter da atlética",
                }
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def save(self, commit=True):
        instance = super().save(False)
        user = User(
            full_name=self.cleaned_data["nome"], email=self.cleaned_data["email"]
        )
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            instance.usuario = user
            instance.save()

        return instance


class AtleticaChangeForm(forms.ModelForm):
    logo = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "placeholder": "Foto",
                "accept": "image/jpeg,image/png,image/jpg",
            }
        ),
    )

    class Meta:
        model = Atletica
        fields = ("nome", "email", "curso", "instagram", "twitter", "logo")
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control form-control-lg", "placeholder": "Email"}
            ),
            "nome": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Nome completo",
                }
            ),
            "curso": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Curso que a atlética pertence",
                }
            ),
            "instagram": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Link da instagram da atlética",
                }
            ),
            "twitter": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Link do Twitter da atlética",
                }
            ),
        }
