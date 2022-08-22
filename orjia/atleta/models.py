from django.db import models


NAIPES = (
    ('F', 'Feminino'),
    ('M', 'Masculino'),
)


class Atleta(models.Model):
    nome = models.CharField('Nome do atleta', max_length=50, null=False, blank=False)
    matricula = models.PositiveIntegerField('Número da matricula', max_length=11, null=False, blank=False)
    chave = models.CharField('Chave de autenticação', max_length=39, null=False, blank=False)
    # atletica = models.ForeignKey(Atletica, on_delete=models.PROTECT, null=False, blank=False)
    naipe = models.CharField('Naipe', max_length=1, choices=NAIPES, null=False, blank=False)
    