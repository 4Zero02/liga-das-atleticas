from django.db import models
from campanha.models import Campanha, Competicao
from modalidade.models import Modalidade
from django.utils.translation import gettext as _


class Atletica(models.Model):
    usuario = models.OneToOneField(User, related_name='usuario_atletica', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=150)
    email = models.CharField(verbose_name='Email', max_length=50, null=True, blank=True)
    curso = models.CharField('Curso', max_length=50, null=False, blank=False)
    instagram = models.CharField('Instagem da Atlética', max_length=40, null=True, blank=True)
    twitter = models.CharField('Twitter da Atlética', max_length=40, null=True, blank=True)
    # is_staff = models.BooleanField(_('Membro da Equipe'), default=False)
    # logo = models.ImageField(upload_to='logos')

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

    nome = models.CharField('Nome do atleta', max_length=50, null=False, blank=False)
    matricula = models.PositiveIntegerField('Número da matricula', null=False, blank=False)
    chave = models.TextField('Chave de autenticação', max_length=39, null=False, blank=False)
    atletica = models.ForeignKey(Atletica, on_delete=models.CASCADE, null=True, blank=True)
    sex = models.CharField(_('Sexo'), max_length=1, choices=Sex.choices, default=Sex.MALE, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', ('Masculino')
        FEMALE = 'F', ('Feminino')
        MIX = 'O', ('Misto')

    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, null=False)
    atletica = models.ForeignKey(Atletica, on_delete=models.CASCADE, null=True, blank=True)
    campanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, null=True, blank=True)
    competicao = models.ForeignKey()
    atleta = models.ManyToManyField(Atleta)
    sex = models.CharField('Sexo', max_length=1, choices=Sex.choices, default=Sex.MALE, null=True)

    class Meta:
        ordering = ['modalidade']
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
