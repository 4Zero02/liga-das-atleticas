from django.urls import path
from . import views as v


app_name = 'base'

urlpatterns = [
    path('', v.home, name='index'),
    path('login/', v.logar, name='login'),
    path('logout/', v.sair, name='sair'),
    # path('cadastrar/', v.SingUp.as_view(), name='cadastrar'),

]
