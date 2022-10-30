from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('', v.home, name='index'),
    path('login/', v.LoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
