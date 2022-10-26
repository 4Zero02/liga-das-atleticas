from django.contrib import admin
from .models import Atletica, Atleta, Equipe, Score


@admin.register(Atletica)
class AtleticaAdmin(admin.ModelAdmin):
    model = Atletica
    list_display = ('nome', 'email', 'curso')


@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    model = Atleta
    list_display = ('nome', 'matricula', 'atletica')
    ordering = ('-atletica',)


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    model = Equipe
    list_display = ('atletica', 'competicao', 'campanha')
    ordering = ('-atletica',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    model = Score
    list_display = ('campanha', 'atletica', 'pontos')
    ordering = ('-campanha', '-atletica')
