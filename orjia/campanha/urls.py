from django.urls import path
from . import views as v

app_name = 'campanha'

urlpatterns = [
    # URLS CAMPANHA
    path('', v.CampanhaList.as_view(), name='campanha_list'),
    path('create/', v.CampanhaCreate.as_view(), name='campanha_create'),
    path('<int:pk>/', v.campanha_detail, name='campanha_detail'),
    path('update/<int:pk>/', v.CampanhaUpdate.as_view(), name='campanha_update'),

    # URLS COMPETIÇÃO
    path('competicao/create/', v.competicao_create, name='competicao_create'),
    path('competicao/update/<int:pk>/', v.CompeticaoUpdate.as_view(), name='competicao_update'),
    path('competicao/<int:pk>/', v.competicao_detail, name='competicao_detail'),
    path('competicao/<int:pk>/ranking', v.ranking, name='competicao_ranking'),
]
