import string
from distutils.command.upload import upload
from random import choice
from django.db import models
from modalidade.models import Modalidade
from datetime import date
import os

# Create your models here.
STATUS = (
    (1, 'ativo'),
    (0, 'inativo'),
)


def create_token(tam=8):
    token = ''
    choices = string.ascii_letters + string.digits
    for i in range(1, tam + 1):
        token += choice(choices)

        if i % 4 == 0 and i != tam:
            token += '.'

    return token.upper()


def upload_photo(instance, filename):
    # /media/logos/<instance.id>-<token_aleatorio>.<extensao_do_arquivo>
    return f"logos/{instance.pk}-{create_token(4)}{os.path.splitext(filename)[-1]}"


class Campanha(models.Model):
    # adm = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=12, null=False, blank=False)
    data_inicio = models.DateField('Data de início', default=date.today)
    data_final = models.DateField('Data de término', default=date.today)
    ano = models.PositiveIntegerField('Ano do evento', null=False, blank=False)
    status = models.CharField(max_length=1, choices=STATUS, default=1)
    # logo = models.ImageField(upload_to='logos/', null=True)

    class Meta:
        ordering = ['ano']
        verbose_name = 'campanha'
        verbose_name_plural = 'campanhas'

    def __str__(self):
        return self.nome


class Competicao(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', ('Masculino')
        FEMALE = 'F', ('Feminino')
        MIX = 'O', ('Misto')

    campanha = models.ForeignKey(Campanha, on_delete=models.PROTECT, null=True, blank=True)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT)
    sex = models.CharField('Sexo', max_length=1, choices=Sex.choices, default=Sex.MALE, null=True)

    class Meta:
        ordering = ['campanha']
        verbose_name = 'competicao'
        verbose_name_plural = 'competicoes'

    def __str__(self):
        nome = "{} - {}".format(self.modalidade, self.sex)
        return nome
