# licentia_process/urls.py
from django.urls import path
from . import views

app_name = 'process'

urlpatterns = [
    path('', views.ProcessListView.as_view(), name='process_list'),
    path('novo/', views.ProcessCreateView.as_view(), name='process_create'),
    path('editar/<int:pk>/', views.ProcessUpdateView.as_view(), name='process_update'),
    path('processos/log/save/', views.SaveProcessLogView.as_view(), name='save_process_log'),
]