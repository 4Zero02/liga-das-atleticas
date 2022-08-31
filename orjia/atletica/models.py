from django.db import models
from django.contrib.auth.models import User


NAIPES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Misto'),
)


class Atletica(models.Model):
    usuario = models.OneToOneField(User, related_name='usuario_atletica', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=150)
    email = models.CharField(verbose_name='E-mail para contato', max_length=50, null=True, blank=True)
    curso = models.CharField('Curso', max_length=50, null=False, blank=False)
    instagram = models.CharField('Instagem da Atlética', max_length=40, null=True, blank=True)
    twitter = models.CharField('Twitter da Atlética', max_length=40, null=True, blank=True)
    # contato =
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
    atletica = models.ForeignKey(Atletica, on_delete=models.CASCADE, null=False, blank=False)
    naipe = models.CharField('Naipe', max_length=1, choices=NAIPES, null=False, blank=False)
    # status = models.CharField() APTO OU NÃO, POREM QUEM DECIDE É A LIGA

    class Meta:
        ordering = ['nome']
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return self.nome

# class Equipe(models.Model):
    # modalidade =
    # atletica =
    # campanha =
    # atleta =
    # naipe =