# Generated by Django 4.1 on 2022-10-19 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atletica', '0003_equipe_competicao_alter_atleta_status_and_more'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competicao',
            name='campanha',
        ),
        migrations.RemoveField(
            model_name='competicao',
            name='modalidade',
        ),
        migrations.DeleteModel(
            name='Campanha',
        ),
        migrations.DeleteModel(
            name='Competicao',
        ),
    ]
