from django.db import models
from django.contrib.auth.models import User


NAIPE = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Misto'),
)

class Atletica(models.Model):
    nome = models.ForeignKey(User, related_name='usuario_atletica', on_delete=models.CASCADE)
    email = models.CharField(verbose_name='E-mail para contato', max_length=50, null=True, blank=True)
    curso = models.CharField('Curso', max_length=50, null=False, blank=False)
    # logo
    instagram = models.CharField('Instagem da Atlética', max_length=40, null=True, blank=True)
    twitter = models.CharField('Twitter da Atlética', max_length=40, null=True, blank=True)
    # contato =


# class Equipe(models.Model):
    # modalidade =
    # atletica =
    # campanha =
    # atleta =
    # naipe =