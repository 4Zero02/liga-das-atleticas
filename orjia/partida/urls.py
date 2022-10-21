from django.urls import path
from . import views as v

app_name = 'partida'

urlpatterns = [
    path('create/<int:pk>', v.partida_create, name='partida_create'),

]
