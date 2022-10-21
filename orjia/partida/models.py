from django.db import models
from atletica.models import Equipe
from campanha.models import Competicao
from datetime import date


# Create your models here.
class Partida(models.Model):
    class Etapa(models.TextChoices):
        PRE = 'P', ('Pre-liminar')
        OITAVAS = 'O', ('Oitavas')
        QUARTAS = 'Q', ('Quartas')
        SEMI = 'S', ('Semi-final')
        TERCEIRO = 'T', ('Terceiro lugar')
        FINAL = 'F', ('Final')

    competicao = models.ForeignKey(Competicao, on_delete=models.PROTECT, null=True)
    numero = models.PositiveIntegerField('Sequencia do jogo', null=True, blank=True)
    data = models.DateField('Data da partida', default=date.today)
    equipeA = models.ForeignKey(Equipe, related_name='Equipe_partida_A', on_delete=models.PROTECT, null=True)
    equipeB = models.ForeignKey(Equipe, related_name='Equipe_partida_B', on_delete=models.PROTECT, null=True)
    equipe_vencedora = models.ForeignKey(Equipe, related_name='Equipe_vencedora', on_delete=models.PROTECT, null=True,
                                         blank=True, default='A definir')
    etapa = models.CharField('Etapa', max_length=1, choices=Etapa.choices, default=Etapa.PRE, null=True)


class Ranking(models.Model):
    competicao = models.OneToOneField(Competicao, on_delete=models.CASCADE, null=True)
    equipe1 = models.ForeignKey(Equipe,
                                related_name='Primeiro_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
    equipe2 = models.ForeignKey(Equipe,
                                related_name='Segundo_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
    equipe3 = models.ForeignKey(Equipe,
                                related_name='Terceiro_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
    equipe4 = models.ForeignKey(Equipe,
                                related_name='Quarto_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
    equipe5 = models.ForeignKey(Equipe,
                                related_name='Quinto_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
    equipe6 = models.ForeignKey(Equipe,
                                related_name='Sexto_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
    equipe7 = models.ForeignKey(Equipe,
                                related_name='Setimo_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
    equipe8 = models.ForeignKey(Equipe,
                                related_name='Oitavo_Lugar',
                                on_delete=models.PROTECT,
                                default='A definir',
                                null=True
                                )
