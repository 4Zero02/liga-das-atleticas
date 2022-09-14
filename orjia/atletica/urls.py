from django.urls import path
from . import views as v


app_name = 'atletica'

urlpatterns = [
    # path('atleta/', v., name='produto_list'),
    path('add/', v.AtleticaCreate.as_view(), name='atletica_add'),
    path('<int:pk>', v.AtleticaDetail.as_view(), name='atletica_detail'),
    path('atleta/add/', v.atleta_add, name='atleta_add'),
]
