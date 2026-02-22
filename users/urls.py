from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registrar/', views.RegistroView.as_view(), name='registrar'),
    path('gerenciar/', views.GerenciarUsuariosView.as_view(), name='gerenciar'),
    path('ativar/<int:pk>/', views.AtivarUsuarioView.as_view(), name='ativar_usuario'),
    path('suspender/<int:pk>/', views.SuspenderUsuarioView.as_view(), name='suspender_usuario'),
]