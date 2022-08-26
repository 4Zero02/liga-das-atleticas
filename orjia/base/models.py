from django.db import models
from datetime import date
from django.contrib.auth.models import User


STATUS = (
    (1, 'ativo'),
    (0, 'inativo'),
)


class Campanha(models.Model):
    nome = models.CharField(max_length=12, null=False, blank=False)
    data_incio = models.DateField('Data de início', default=date.today)
    data_final = models.DateField('Data de término', default=date.today)
    ano = models.PositiveIntegerField('Ano do evento', null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS)


# Verificar a informações necessárias aqui
class LigaUser(models.Model):
    usuario = models.OneToOneField(User, related_name='usuario_liga', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=200)
