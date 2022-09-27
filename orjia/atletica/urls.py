from django.urls import path
from . import views as v

app_name = 'atletica'

urlpatterns = [
    path('', v.AtleticaList.as_view(), name='atletica_list'),
    path('add/', v.AtleticaCreate.as_view(), name='atletica_add'),
    path('<int:pk>', v.AtleticaDetail.as_view(), name='atletica_detail'),
    path('update/<int:pk>', v.AtleticaUpdate.as_view(), name='atletica_update'),

    # URLS ATLETAS
    path('atleta/list', v.atleta_list, name='atleta_list'),
    path('atleta/add/', v.atleta_add, name='atleta_add'),
    path('atleta/update/<int:pk>', v.AtletaUpdate.as_view(), name='atleta_update'),
    path('atleta/delete/<int:pk>', v.atleta_delete, name='atleta_delete'),

    # URLS EQUIPES
    path('equipe/add', v.EquipeCreate.as_view(), name='equipe_create'),
]
