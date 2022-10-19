from django.urls import path
from . import views as v

app_name = 'partida'

urlpatterns = [
    path('', v.AtleticaList.as_view(), name='atletica_list'),

]
