# Generated by Django 4.1 on 2022-11-04 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("atletica", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="atletica",
            name="usuario",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usuario_atletica",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="atleta",
            name="atletica",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="atletica.atletica",
            ),
        ),
    ]
