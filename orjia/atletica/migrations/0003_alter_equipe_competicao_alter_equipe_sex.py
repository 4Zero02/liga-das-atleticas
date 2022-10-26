# Generated by Django 4.1 on 2022-10-26 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campanha', '0001_initial'),
        ('atletica', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='competicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campanha.competicao'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='sex',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Sexo'),
        ),
    ]
