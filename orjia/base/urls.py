from django.urls import path
from . import views as v

app_name = 'base'

urlpatterns = [
    path('', v.home, name='index'),
    path('campanha/cadastro', v.campanha_create, name='campanha_create'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
]
