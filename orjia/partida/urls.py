from django.urls import path
from .views import CompeticaoResultadoUpdate
from . import views as v

app_name = "partida"

urlpatterns = [
    path("create/<int:pk>", v.partida_create, name="partida_create"),
    path("update/<int:pk>", v.PartidaUpdate.as_view(), name="partida_update"),
    path("<int:pk>/", v.partida_detail, name="partida_detail"),
    path(
        "gerenciar_resultados/<int:partida_pk>",
        CompeticaoResultadoUpdate.as_view(),
        name="gerenciar_resultados",
    ),
]
