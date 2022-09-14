from django.urls import path
from . import views as v

app_name = 'atletica'

urlpatterns = [
    path('', v.atletica_list, name='atletica_list'),
    path('atleta/add/', v.atleta_add, name='atleta_add'),
    path('add/', v.AtleticaCreate.as_view(), name='atletica_add'),
    path('<int:pk>', v.AtleticaDetail.as_view(), name='atletica_detail'),
]
