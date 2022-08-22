from django.db import models
from datetime import date


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
