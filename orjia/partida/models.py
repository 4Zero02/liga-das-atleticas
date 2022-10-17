from django.db import models
from atletica.models import Equipe
from orjia.campanha.models import Competicao


# Create your models here.
class Partida(models.Model):
    # modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
    # campanha = models.ForeignKey(Campanha, on_delete=models.PROTECT)
    competicao = models.ForeignKey(Competicao, on_delete=models.PROTECT)
    equipe = models.ManyToManyField(Equipe)
    # resultado =