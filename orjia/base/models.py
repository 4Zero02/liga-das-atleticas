from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils.translation import gettext as _


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(_('Nome Completo'), max_length=255)
    cpf = models.CharField(
        _('CPF'),
        unique=True,
        error_messages={'unique': _("Já existe um usuário com este CPF")},
        max_length=15,
        null=True
    )
    email = models.EmailField(
        _('Email'),
        unique=True,
        error_messages={'unique': _("Já existe um usuário com este email")},
    )
    is_staff = models.BooleanField(_('Membro da Equipe'), default=False)
    is_active = models.BooleanField(
        _('Ativo'), default=True, help_text=_('Desative para tirar o acesso do usuário')
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    def __str__(self):
        return f'{self.email} {self.full_name[:30]}'
