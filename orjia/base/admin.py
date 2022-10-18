from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ('full_name', 'cpf')
