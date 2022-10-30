from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('atletica/', include('atletica.urls')),
    path('modalidade/', include('modalidade.urls')),
    path('campanha/', include('campanha.urls')),
    path('partida/', include('partida.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)