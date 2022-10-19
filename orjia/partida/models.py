from django.db import models
from atletica.models import Equipe
from campanha.models import Competicao
from datetime import date


# Create your models here.
class Partida(models.Model):
    competicao = models.ForeignKey(Competicao, on_delete=models.PROTECT)
    equipe = models.ManyToManyField(Equipe)
    data = models.DateField('Data de início', default=date.today)
    # equipes = models.ManyToManyField(Equipe)
    # equipe_vencedora = models.ForeignKey(Equipe, on_delete=models.PROTECT, null=True, blank=True)
    # etapa = models.Choices()


# class Ranking(models.Model):
#     competicao = models.OneToOneField(Competicao, on_delete=models.CASCADE)
#     equipe1 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
#     equipe2 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
#     equipe3 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
#     equipe4 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
#     equipe5 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
#     equipe6 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
#     equipe7 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
#     equipe8 = models.ForeignKey(Equipe, on_delete=models.PROTECT)
