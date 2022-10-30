from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as v

app_name = 'atletica'

urlpatterns = [
    path('', v.AtleticaList.as_view(), name='atletica_list'),
    path('add/', v.AtleticaCreate.as_view(), name='atletica_add'),
    path('<int:pk>', v.AtleticaDetail.as_view(), name='atletica_detail'),
    path('update/<int:pk>', v.AtleticaUpdate.as_view(), name='atletica_update'),
    path('delete/<int:pk>', v.AtleticaDelete.as_view(), name='atletica_delete'),

    # URLS ATLETAS
    path('atleta/list', v.atleta_list, name='atleta_list'),
    path('atleta/add/', v.atleta_add, name='atleta_add'),
    path('atleta/update/<int:pk>', v.AtletaUpdate.as_view(), name='atleta_update'),
    path('atleta/delete/<int:pk>', v.atleta_delete, name='atleta_delete'),

    # URLS EQUIPES
    path('equipe/', v.equipe_list, name='equipe_list'),
    path('equipe/add', v.equipe_create, name='equipe_create'),
    path('equipe/delete/<int:pk>', v.equipe_delete, name='equipe_delete'),
    path('equipe/update/<int:pk>', v.EquipeUpdate.as_view(), name='equipe_update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)