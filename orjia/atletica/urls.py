from django.urls import path
from . import views as v

app_name = 'atletica'

urlpatterns = [
    path('', v.AtleticaList.as_view(), name='atletica_list'),
    path('add/', v.AtleticaCreate.as_view(), name='atletica_add'),
    path('<int:pk>', v.AtleticaDetail.as_view(), name='atletica_detail'),
    path('update/<int:pk>', v.AtleticaUpdate.as_view(), name='atletica_update'),
    path('atleta/add/', v.atleta_add, name='atleta_add'),
]
