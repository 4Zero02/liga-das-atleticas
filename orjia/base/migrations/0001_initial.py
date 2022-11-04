# Generated by Django 4.1 on 2022-11-04 01:51

import base.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=255, verbose_name="Nome Completo"),
                ),
                (
                    "cpf",
                    models.CharField(
                        error_messages={"unique": "Já existe um usuário com este CPF"},
                        max_length=15,
                        null=True,
                        unique=True,
                        verbose_name="CPF",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "Já existe um usuário com este email"
                        },
                        max_length=254,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Membro da Equipe"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Desative para tirar o acesso do usuário",
                        verbose_name="Ativo",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
                "verbose_name_plural": "Usuários",
            },
            managers=[
                ("objects", base.managers.UserManager()),
            ],
        ),
    ]
