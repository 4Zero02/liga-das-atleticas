# Generated by Django 4.1 on 2022-09-20 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modalidade', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modalidade',
            options={'ordering': ['nome'], 'verbose_name': 'Modalidade', 'verbose_name_plural': 'Modalidades'},
        ),
    ]
