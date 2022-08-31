# Generated by Django 4.1 on 2022-08-29 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atletica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='E-mail para contato')),
                ('curso', models.CharField(max_length=50, verbose_name='Curso')),
                ('instagram', models.CharField(blank=True, max_length=40, null=True, verbose_name='Instagem da Atlética')),
                ('twitter', models.CharField(blank=True, max_length=40, null=True, verbose_name='Twitter da Atlética')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_atletica', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Atlética',
                'verbose_name_plural': 'Atléticas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do atleta')),
                ('matricula', models.PositiveIntegerField(verbose_name='Número da matricula')),
                ('chave', models.CharField(max_length=39, verbose_name='Chave de autenticação')),
                ('naipe', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Misto')], max_length=1, verbose_name='Naipe')),
                ('atletica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atletica.atletica')),
            ],
            options={
                'verbose_name': 'Atleta',
                'verbose_name_plural': 'Atletas',
                'ordering': ['nome'],
            },
        ),
    ]