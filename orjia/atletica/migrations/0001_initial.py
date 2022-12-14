# Generated by Django 4.1 on 2022-11-04 01:51

import atletica.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("campanha", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Atleta",
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
                    "nome",
                    models.CharField(max_length=50, verbose_name="Nome do atleta"),
                ),
                (
                    "matricula",
                    models.PositiveIntegerField(verbose_name="Número da matricula"),
                ),
                (
                    "chave",
                    models.TextField(
                        max_length=39, verbose_name="Chave de autenticação"
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Feminino")],
                        default="M",
                        max_length=1,
                        null=True,
                        verbose_name="Sexo",
                    ),
                ),
                ("status", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Atleta",
                "verbose_name_plural": "Atletas",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Atletica",
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
                ("nome", models.CharField(max_length=150, verbose_name="Nome")),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Email"
                    ),
                ),
                ("curso", models.CharField(max_length=50, verbose_name="Curso")),
                (
                    "instagram",
                    models.CharField(
                        blank=True,
                        max_length=40,
                        null=True,
                        verbose_name="Instagem da Atlética",
                    ),
                ),
                (
                    "twitter",
                    models.CharField(
                        blank=True,
                        max_length=40,
                        null=True,
                        verbose_name="Twitter da Atlética",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        null=True, upload_to=atletica.models.upload_photo
                    ),
                ),
            ],
            options={
                "verbose_name": "Atlética",
                "verbose_name_plural": "Atléticas",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Score",
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
                ("pontos", models.PositiveIntegerField(default=0, null=True)),
                (
                    "atletica",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="atletica.atletica",
                    ),
                ),
                (
                    "campanha",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="campanha.campanha",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pontuação",
                "verbose_name_plural": "Pontuação",
                "ordering": ["pontos"],
            },
        ),
        migrations.CreateModel(
            name="Equipe",
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
                    "sex",
                    models.CharField(
                        blank=True, max_length=1, null=True, verbose_name="Sexo"
                    ),
                ),
                ("atleta", models.ManyToManyField(to="atletica.atleta")),
                (
                    "atletica",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="atletica.atletica",
                    ),
                ),
                (
                    "campanha",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="campanha.campanha",
                    ),
                ),
                (
                    "competicao",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="campanha.competicao",
                    ),
                ),
            ],
            options={
                "verbose_name": "Equipe",
                "verbose_name_plural": "Equipes",
                "ordering": ["competicao"],
            },
        ),
    ]
