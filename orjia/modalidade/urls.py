from django.urls import path
from . import views as v


app_name = 'modalidade'

urlpatterns = [
    path('', v.modalidade_list, name='modalidade_list'),
    path('add/', v.modalidade_add, name='modalidade_add'),
]
