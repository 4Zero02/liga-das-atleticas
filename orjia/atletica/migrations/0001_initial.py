# Generated by Django 4.1 on 2022-09-27 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do atleta')),
                ('matricula', models.PositiveIntegerField(verbose_name='Número da matricula')),
                ('chave', models.CharField(max_length=39, verbose_name='Chave de autenticação')),
                ('naipe', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Naipe')),
            ],
            options={
                'verbose_name': 'Atleta',
                'verbose_name_plural': 'Atletas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Atletica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('curso', models.CharField(max_length=50, verbose_name='Curso')),
                ('instagram', models.CharField(blank=True, max_length=40, null=True, verbose_name='Instagem da Atlética')),
                ('twitter', models.CharField(blank=True, max_length=40, null=True, verbose_name='Twitter da Atlética')),
            ],
            options={
                'verbose_name': 'Atlética',
                'verbose_name_plural': 'Atléticas',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atleta', models.ManyToManyField(to='atletica.atleta')),
                ('atletica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atletica.atletica')),
            ],
        ),
    ]
