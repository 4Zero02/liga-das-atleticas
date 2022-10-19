from django.contrib import admin
from .models import Campanha, Competicao


# Register your models here.
@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    model = Campanha
    list_display = ('nome', 'ano')


@admin.register(Competicao)
class CompeticaoAdmin(admin.ModelAdmin):
    model = Competicao
    list_display = ('campanha', 'modalidade', 'sex')
    ordering = ('-campanha', 'modalidade')
