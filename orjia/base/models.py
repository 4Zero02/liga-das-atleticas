from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils.translation import gettext as _
from modalidade.models import Modalidade
# from atletica.models import Equipe


STATUS = (
    (1, 'ativo'),
    (0, 'inativo'),
)


class Campanha(models.Model):
    nome = models.CharField(max_length=12, null=False, blank=False)
    # adm = models.ForeignKey(User, on_delete=models.PROTECT)
    data_inicio = models.DateField('Data de início', default=date.today)
    data_final = models.DateField('Data de término', default=date.today)
    ano = models.PositiveIntegerField('Ano do evento', null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS, default=0)

    class Meta:
        verbose_name = 'campanha'
        verbose_name_plural = 'campanhas'


class Competicao(models.Model):
    campanha = models.ForeignKey(Campanha, on_delete=models.PROTECT)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
    data = models.DateField('Data da competição', default=date.today)
    # equipes = models.ManyToManyField(Equipe)

    class Meta:
        verbose_name = 'competicao'
        verbose_name_plural = 'competicoes'


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
