from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Rota do App Core (Home)
    path('', include('core.urls')),
    
    # Rota do App Users (para futuras gestões de perfil)
    path('users/', include('users.urls', namespace='users')),

    path('recursos/', include('licentia_resources.urls')),

    path('processos/', include('licentia_process.urls')),
]

# Configuração para servir arquivos de mídia (imagens/PDFs dos recursos) em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)