from django.db import models
from base.models import User
from modalidade.models import Modalidade
from base.models import Campanha
from django.utils.translation import gettext as _


NAIPES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)


class Atletica(models.Model):
    usuario = models.OneToOneField(User, related_name='usuario_atletica', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=150)
    email = models.CharField(verbose_name='Email', max_length=50, null=True, blank=True)
    curso = models.CharField('Curso', max_length=50, null=False, blank=False)
    instagram = models.CharField('Instagem da Atlética', max_length=40, null=True, blank=True)
    twitter = models.CharField('Twitter da Atlética', max_length=40, null=True, blank=True)
    # is_staff = models.BooleanField(_('Membro da Equipe'), default=False)
    # logo

    class Meta:
        ordering = ['nome']
        verbose_name = 'Atlética'
        verbose_name_plural = 'Atléticas'

    def __str__(self):
        return self.nome


class Atleta(models.Model):
    nome = models.CharField('Nome do atleta', max_length=50, null=False, blank=False)
    matricula = models.PositiveIntegerField('Número da matricula', null=False, blank=False)
    chave = models.CharField('Chave de autenticação', max_length=39, null=False, blank=False)
    atletica = models.ForeignKey(Atletica, on_delete=models.CASCADE, null=True, blank=True)
    naipe = models.CharField('Naipe', max_length=1, choices=NAIPES, null=False, blank=False)
    # status = models.CharField() APTO OU NÃO, POREM QUEM DECIDE É A LIGA

    class Meta:
        ordering = ['nome']
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, null=False)
    atletica = models.ForeignKey(Atletica, on_delete=models.CASCADE, null=False)
    # campanha vai ser setada diretamente como a campanha ativa
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, null=True)
    atleta = models.ManyToManyField(Atleta)
