from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    # Projetos
    path('projetos/', views.ProjetoListView.as_view(), name='projeto_list'),
    path('projetos/novo/', views.ProjetoCreateView.as_view(), name='projeto_create'),
    path('projetos/<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='projeto_update'),

    # Componentes
    path('componentes/', views.ComponenteListView.as_view(), name='componente_list'),
    path('componentes/novo/', views.ComponenteCreateView.as_view(), name='componente_create'),
    path('componentes/<int:pk>/editar/', views.ComponenteUpdateView.as_view(), name='componente_update'),

    # Status do Processo
    path('status-processo/', views.StatusDoProcessoListView.as_view(), name='statusdoprocesso_list'),
    path('status-processo/novo/', views.StatusDoProcessoCreateView.as_view(), name='statusdoprocesso_create'),
    path('status-processo/<int:pk>/editar/', views.StatusDoProcessoUpdateView.as_view(), name='statusdoprocesso_update'),

#     # Status Pagamento Freela
#     path('status-pagamento-freela/', views.StatusPagamentoFreelaListView.as_view(), name='status_pagamento_freela_list'),
#     path('status-pagamento-freela/novo/', views.StatusPagamentoFreelaCreateView.as_view(), name='status_pagamento_freela_create'),
#     path('status-pagamento-freela/<int:pk>/editar/', views.StatusPagamentoFreelaUpdateView.as_view(), name='status_pagamento_freela_update'),
]