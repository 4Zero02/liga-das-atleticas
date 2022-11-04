# Generated by Django 4.1 on 2022-11-04 01:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("atletica", "0001_initial"),
        ("campanha", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Competidor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qualificador", models.CharField(max_length=1, null=True)),
                (
                    "resultado",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        null=True,
                        verbose_name="Resultado da equipe",
                    ),
                ),
                (
                    "equipe",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="atletica.equipe",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ranking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "competicao",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="campanha.competicao",
                    ),
                ),
                (
                    "equipe1",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Primeiro_Lugar",
                        to="atletica.equipe",
                    ),
                ),
                (
                    "equipe2",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Segundo_Lugar",
                        to="atletica.equipe",
                    ),
                ),
                (
                    "equipe3",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Terceiro_Lugar",
                        to="atletica.equipe",
                    ),
                ),
                (
                    "equipe4",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Quarto_Lugar",
                        to="atletica.equipe",
                    ),
                ),
                (
                    "equipe5",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Quinto_Lugar",
                        to="atletica.equipe",
                    ),
                ),
                (
                    "equipe6",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Sexto_Lugar",
                        to="atletica.equipe",
                    ),
                ),
                (
                    "equipe7",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Setimo_Lugar",
                        to="atletica.equipe",
                    ),
                ),
                (
                    "equipe8",
                    models.ForeignKey(
                        default="A definir",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="Oitavo_Lugar",
                        to="atletica.equipe",
                    ),
                ),
            ],
            options={
                "verbose_name": "ranking",
                "verbose_name_plural": "rankings",
            },
        ),
        migrations.CreateModel(
            name="Partida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "numero",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Sequencia do jogo"
                    ),
                ),
                (
                    "data",
                    models.DateField(
                        default=datetime.date.today, verbose_name="Data da partida"
                    ),
                ),
                (
                    "local",
                    models.CharField(
                        default="A definir",
                        max_length=255,
                        null=True,
                        verbose_name="Local do jogo",
                    ),
                ),
                (
                    "md",
                    models.CharField(
                        choices=[
                            ("1", "Um (1)"),
                            ("3", "Tres (3)"),
                            ("5", "Cinco (5)"),
                        ],
                        default=1,
                        max_length=1,
                        verbose_name="Melhor de:",
                    ),
                ),
                (
                    "unidade",
                    models.CharField(
                        choices=[
                            ("P", "Pontos"),
                            ("S", "Sets"),
                            ("G", "Gols"),
                            ("T", "Segundos"),
                            ("M", "Minutos"),
                            ("R", "Rodadas"),
                            ("O", "Geral"),
                        ],
                        default="O",
                        max_length=1,
                        null=True,
                        verbose_name="Unidade",
                    ),
                ),
                (
                    "etapa",
                    models.CharField(
                        choices=[
                            ("P", "Pre-liminar"),
                            ("O", "Oitavas"),
                            ("Q", "Quartas"),
                            ("D", "Quartas-desempate | Quinto e Sexto"),
                            ("U", "Quartas-desempate | Setimo e Oitavo"),
                            ("S", "Semi-final"),
                            ("T", "Terceiro lugar"),
                            ("F", "Final"),
                        ],
                        default="P",
                        max_length=1,
                        null=True,
                        verbose_name="Etapa",
                    ),
                ),
                (
                    "competicao",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="campanha.competicao",
                    ),
                ),
                (
                    "equipes",
                    models.ManyToManyField(
                        through="partida.Competidor", to="atletica.equipe"
                    ),
                ),
            ],
            options={
                "verbose_name": "partida",
                "verbose_name_plural": "partidas",
                "ordering": ["numero"],
            },
        ),
        migrations.AddField(
            model_name="competidor",
            name="partida",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="partida.partida",
            ),
        ),
    ]
