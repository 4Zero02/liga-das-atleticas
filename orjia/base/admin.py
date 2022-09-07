from django.contrib import admin
from .models import User, Campanha


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('full_name', 'cpf')


@admin.register(Campanha)
class CampanhaAdmin(admin.ModelAdmin):
    model = Campanha
    list_display = ('nome', 'ano')
