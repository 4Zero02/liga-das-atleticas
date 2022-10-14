from django.db import models
from modalidade.models import Modalidade
from datetime import date
from atletica.models import Equipe

# Create your models here.
STATUS = (
    (1, 'ativo'),
    (0, 'inativo'),
)


class Campanha(models.Model):
    # adm = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=12, null=False, blank=False)
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

    class Meta:
        verbose_name = 'competicao'
        verbose_name_plural = 'competicoes'


class Partida(models.Model):
    # modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
    # campanha = models.ForeignKey(Campanha, on_delete=models.PROTECT)
    competicao = models.ForeignKey(Competicao, on_delete=models.PROTECT)
    equipe = models.ManyToManyField(Equipe)
    # resultado =


# class Ranking(models.Model):
#     pass
