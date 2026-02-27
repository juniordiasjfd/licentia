from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('registrar/', views.RegistroView.as_view(), name='registrar'),
    path('gerenciar/', views.GerenciarUsuariosView.as_view(), name='gerenciar'),
    path('departamentos/', views.DepartamentoListView.as_view(), name='departamento_list'),
    path('departamentos/novo/', views.DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/<int:pk>/editar/', views.DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('ativar/<int:pk>/', views.AtivarUsuarioView.as_view(), name='ativar_usuario'),
    path('suspender/<int:pk>/', views.SuspenderUsuarioView.as_view(), name='suspender_usuario'),
    path('configuracoes/', views.UserSettingsUpdateView.as_view(), name='settings'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),
]