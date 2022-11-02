from django.db import models
from campanha.models import Campanha, Competicao, create_token
from django.utils.translation import gettext as _
from base.models import User
import os


def upload_photo(instance, filename):
    # /media/logos/<instance.id>-<token_aleatorio>.<extensao_do_arquivo>
    return f"logos/{instance.nome}-{create_token(4)}{os.path.splitext(filename)[-1]}"


class Atletica(models.Model):
    usuario = models.OneToOneField(User, related_name='usuario_atletica', on_delete=models.CASCADE)
    nome = models.CharField(verbose_name='Nome', max_length=150)
    email = models.CharField(verbose_name='Email', max_length=50, null=True, blank=True)
    curso = models.CharField(verbose_name='Curso', max_length=50, null=False, blank=False)
    instagram = models.CharField(verbose_name='Instagem da Atlética', max_length=40, null=True, blank=True)
    twitter = models.CharField(verbose_name='Twitter da Atlética', max_length=40, null=True, blank=True)
    logo = models.ImageField(upload_to=upload_photo, null=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Atlética'
        verbose_name_plural = 'Atléticas'

    def __str__(self):
        return self.nome


class Atleta(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', _('Masculino')
        FEMALE = 'F', _('Feminino')

    nome = models.CharField(verbose_name='Nome do atleta', max_length=50, null=False, blank=False)
    matricula = models.PositiveIntegerField(verbose_name='Número da matricula', null=False, blank=False)
    chave = models.TextField(verbose_name='Chave de autenticação', max_length=39, null=False, blank=False)
    atletica = models.ForeignKey(Atletica, on_delete=models.CASCADE, null=True, blank=True)
    sex = models.CharField(verbose_name=_('Sexo'), max_length=1, choices=Sex.choices, default=Sex.MALE, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    atletica = models.ForeignKey(Atletica, on_delete=models.CASCADE, null=True, blank=True)
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, null=True, blank=True)
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE, null=True, blank=True)
    atleta = models.ManyToManyField(Atleta)
    sex = models.CharField('Sexo', max_length=1, null=True, blank=True)

    class Meta:
        ordering = ['competicao']
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __str__(self):
        nome = '{} - {}'.format(self.atletica.nome, self.competicao.modalidade.nome)
        return nome


class Score(models.Model):
    atletica = models.ForeignKey(Atletica, on_delete=models.PROTECT)
    campanha = models.ForeignKey(Campanha, on_delete=models.PROTECT)
    pontos = models.PositiveIntegerField()

    class Meta:
        ordering = ['pontos']
        verbose_name = 'Pontuação'
        verbose_name_plural = 'Pontuação'
