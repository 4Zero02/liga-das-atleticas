from django.db import models
from django.urls import reverse_lazy

TIPO_EQUIPE = (
    ('C', 'Coletiva'),
    ('I', 'Individual'),
    ('V', 'Virtual'),
    ('M', 'Mesa')
)


TIPO_CONFRONTO = (
    (0, 'Mata-mata'),
    (1, 'Todos-x-todos')
)


class Modalidade(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    tipo = models.CharField(max_length=1, choices=TIPO_EQUIPE)
    max_atletas = models.PositiveIntegerField()
    min_atletas = models.PositiveIntegerField()
    tipo_confronto = models.CharField(max_length=1, choices=TIPO_CONFRONTO)
    eh_misto = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse_lazy('modalidade:modalidade_list')

    def __str__(self):
        return self.nome
