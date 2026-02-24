from django.urls import path
from . import views
import re

app_name = 'resources'

# Lista de modelos que seguem o padrão List/Create/Update
modelos_recursos = [
    'Projeto', 'Componente', 'StatusDoProcesso', 'StatusDoOrcamento',
    'StatusDoOrcamentoAprovacao', 'StatusDoProcessoPagamentoFornecedor',
    'StatusDoFreelaPagamento', 'StatusAnaliseEditorial', 'StatusAnaliseAutRec',
    'LocalizacaoDoRecurso', 'Fornecedor', 'Empresa', 'CentroDeCusto',
    'TipoDeTermo', 'LimitacaoEdicao'
]

urlpatterns = []

for modelo in modelos_recursos:
    # 1. model_name_lower: Nome técnico usado internamente (ex: statusdoorcamentoaprovacao)
    # Importante para o 'name=' da URL ser compatível com seu context_processor
    model_internal_name = modelo.lower()
    
    # 2. url_path: Nome amigável para o navegador (ex: status-orcamento-aprovacao)
    # Aqui transformamos CamelCase em kebab-case
    url_path = re.sub(r'(?<!^)(?=[A-Z])', '-', modelo).lower()

    # Busca as classes de view dinamicamente
    list_view = getattr(views, f'{modelo}ListView')
    create_view = getattr(views, f'{modelo}CreateView')
    update_view = getattr(views, f'{modelo}UpdateView')

    urlpatterns += [
        path(f'{url_path}/', list_view.as_view(), name=f'{model_internal_name}_list'),
        path(f'{url_path}/novo/', create_view.as_view(), name=f'{model_internal_name}_create'),
        path(f'{url_path}/<int:pk>/editar/', update_view.as_view(), name=f'{model_internal_name}_update'),
    ]

