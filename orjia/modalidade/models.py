from django.db import models


TIPO_EQUIPE = (
    ('C', 'Coletiva'),
    ('I', 'Individual'),
    ('V', 'Virtual'),
    ('M', 'Mesa')
)

NAIPES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Misto')
)

TIPO_CONFRONTO = (
    ('0', 'Mata-mata'),
    ('1', 'Todos-x-todos')
)


class Modalidade(models.Model):
    nome = models.CharField(max_length=12, null=False, blank=False)
    tipo = models.CharField(max_length=1, choices=TIPO_EQUIPE)
    max_atletas = models.PositiveIntegerField()
    min_atletas = models.PositiveIntegerField()
    naipe = models.CharField(max_length=1, choices=NAIPES)
    tipo_confronto = models.CharField(max_length=1, choices=TIPO_CONFRONTO)
