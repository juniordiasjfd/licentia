from django.urls import path
from .views import HomeView, InstrucoesView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('primeiros-passos/', InstrucoesView.as_view(), name='tela_de_instrucoes'),
]