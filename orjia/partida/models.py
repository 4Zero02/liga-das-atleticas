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
        DESEMPATE = 'D', ('Quartas-desempate')
        SEMI = 'S', ('Semi-final')
        TERCEIRO = 'T', ('Terceiro lugar')
        FINAL = 'F', ('Final')

    competicao = models.ForeignKey(Competicao, on_delete=models.PROTECT, null=True, blank=True)
    numero = models.PositiveIntegerField('Sequencia do jogo', null=True, blank=True)
    data = models.DateField('Data da partida', default=date.today)
    local = models.CharField('Local do jogo', max_length=255, null=True, default='A definir')
    equipes = models.ManyToManyField(Equipe, through='Competidor')
    etapa = models.CharField('Etapa', max_length=1, choices=Etapa.choices, default=Etapa.PRE, null=True)

    class Meta:
        ordering = ['numero']
        verbose_name = 'partida'
        verbose_name_plural = 'partidas'


class Competidor(models.Model):
    class Unidade(models.TextChoices):
        PONTOS = 'P', ('Pontos')
        SETS = 'S', ('Sets')
        GOLS = 'G', ('Gols')
        SEC = 'T', ('Segundos')
        MIN = 'M', ('Minutos')
        ROUNDS = 'R', ('Rodadas')
        GERAL = 'O', ('Geral')
        # RODADAS = 'O', ('Misto')

    equipe = models.ForeignKey(Equipe, on_delete=models.PROTECT, null=True)
    partida = models.ForeignKey(Partida, on_delete=models.PROTECT, null=True)
    qualificador = models.CharField(max_length=1, null=True)
    resultado = models.PositiveIntegerField('Resultado da equipe', null=True, blank=True)
    unidade = models.CharField('Unidade', choices=Unidade.choices, max_length=1, default=Unidade.GERAL, null=True)


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

    class Meta:
        verbose_name = 'ranking'
        verbose_name_plural = 'rankings'
