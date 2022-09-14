from django.urls import path
from . import views as v


app_name = 'modalidade'

urlpatterns = [
    path('', v.modalidade_list, name='modalidade_list'),
    path('add/', v.modalidade_add, name='modalidade_add'),
    path('edit/<int:pk>', v.ModalidadeUpdate.as_view(), name='modalidade_edit'),
    path('delete/<int:pk>', v.ModalidadeUpdate.as_view(), name='modalidade_delete'),
]
