from django.contrib import admin
from .models import Atletica


@admin.register(Atletica)
class AtleticaAdmin(admin.ModelAdmin):
    model = Atletica
    list_display = ('usuario', 'nome', 'curso')

