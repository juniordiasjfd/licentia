# licentia_process/urls.py
from django.urls import path
from . import views

app_name = 'process'

urlpatterns = [
    path('', views.ProcessListView.as_view(), name='process_list'),
    path('novo/', views.ProcessCreateView.as_view(), name='process_create'),
    path('<int:pk>/editar/', views.ProcessUpdateView.as_view(), name='process_update'),
]