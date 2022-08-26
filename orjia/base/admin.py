from django.contrib import admin
from .models import LigaUser, Campanha


@admin.register(LigaUser)
class LigaUserAdmin(admin.ModelAdmin):
    model = LigaUser
    list_display = ('usuario', 'nome')

@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    model = Campanha
    list_display = ('nome', 'ano')
