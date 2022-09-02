from django.urls import path
from . import views as v


app_name = 'atletica'

urlpatterns = [
    # path('atleta/', v., name='produto_list'),
    path('add/', v.atletica_add, name='atletica_add'),
    path('atleta/add/', v.atleta_add, name='atleta_add'),
]
