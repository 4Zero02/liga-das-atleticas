from django.urls import path
from . import views as v


app_name = 'atletica'

urlpatterns = [
    # path('', v., name='produto_list'),
    path('atleta/add/', v.atleta_add, name='atleta_add'),
]
