from django.urls import path
from . import views as v

app_name = 'campanha'

urlpatterns = [
    path('cadastro/', v.campanha_create, name='campanha_create'),
]
