from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib import messages

User = get_user_model()


# class UserForm(forms.ModelForm):
#     error_messages = {
#         'password_mismatch': _('The two password fields didnt match.'),
#     }
#     password1 = forms.CharField(
#         label=_("Senha"), strip=False, widget=forms.PasswordInput(
#             attrs={'autocomplete': 'new-password', 'class': 'form-control form-control-lg', 'placeholder': 'Senha'})
#     )
#     password2 = forms.CharField(
#         label=_("Confirmar senha"), strip=False,
#         widget=forms.PasswordInput(
#             attrs={
#                 'autocomplete': 'new-password',
#                 'class': 'form-control form-control-lg',
#                 'placeholder': 'Confirmação de senha'
#             }
#         )
#     )
#
#     class Meta:
#         model = User
#         fields = ('full_name', 'email', 'password1', 'password2')
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}),
#             'full_name': forms.TextInput(
#                 attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome completo'}
#             )
#         }
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'], code='password_mismatch',
#             )
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


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
