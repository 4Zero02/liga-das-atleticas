# Generated by Django 4.1 on 2022-10-20 04:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modalidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=12)),
                ('data_inicio', models.DateField(default=datetime.date.today, verbose_name='Data de início')),
                ('data_final', models.DateField(default=datetime.date.today, verbose_name='Data de término')),
                ('ano', models.PositiveIntegerField(verbose_name='Ano do evento')),
                ('status', models.CharField(choices=[(1, 'ativo'), (0, 'inativo')], default=1, max_length=1)),
            ],
            options={
                'verbose_name': 'campanha',
                'verbose_name_plural': 'campanhas',
            },
        ),
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Misto')], default='M', max_length=1, null=True, verbose_name='Sexo')),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campanha.campanha')),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modalidade.modalidade')),
            ],
            options={
                'verbose_name': 'competicao',
                'verbose_name_plural': 'competicoes',
            },
        ),
    ]