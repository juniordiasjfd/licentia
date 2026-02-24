# licentia_process/admin.py
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Process

@admin.register(Process)
class ProcessAdmin(SimpleHistoryAdmin):
    # Campos exibidos na lista principal
    list_display = ('retranca', 'titulo_descricao', 'projeto', 'status_do_processo', 'data_entrada')
    list_filter = ('projeto', 'status_do_processo', 'empresa', 'data_entrada')
    search_fields = ('retranca', 'titulo_descricao', 'obra_original')
    filter_horizontal = ('atribuido_a',) # Melhora a seleção de múltiplos usuários

    # Organização do formulário em grupos (Fieldsets)
    fieldsets = (
        ('Identificação e Localização', {
            'fields': (
                ('retranca', 'projeto', 'componente'),
                ('titulo_descricao', 'solicitado_para'),
                ('volume', 'pagina', 'unidade', 'lote'),
            )
        }),
        ('Conteúdo e Mídia', {
            'fields': ('obra_original', 'codigo_biblioteca_link', ('solicitar_imagem', 'enviar_formulario'))
        }),
        ('Fluxo de Análise', {
            'fields': (
                ('status_analise_editorial', 'status_analise_autrec'),
                ('data_entrada', 'data_analise_autrec'),
                'localizacao_do_recurso'
            )
        }),
        ('Financeiro e Contratação', {
            'fields': (
                ('fornecedor', 'valor_do_processo'),
                ('empresa', 'centro_de_custo'),
                ('status_do_orcamento', 'status_do_orcamento_aprovacao'),
            )
        }),
        ('Status Final e Pagamentos', {
            'fields': (
                'status_do_processo',
                'status_do_processo_pagamento_fornecedor',
                'status_do_freela_pagamento'
            )
        }),
        ('Direitos e Limitações', {
            'fields': (
                'tipo_de_termo',
                ('limitacao_anos', 'limitacao_tiragem', 'limitacao_edicao'),
                'limitacao_outros'
            )
        }),
        ('Textos Detalhados', {
            'classes': ('collapse',), # Oculto por padrão para não poluir a tela
            'fields': ('observacao_editorial', 'credito_obrigatorio', 'observacao_autrec')
        }),
        ('Atribuição', {
            'fields': ('atribuido_a',)
        }),
    )

    # Configuração para que o histórico registre o utilizador logado
    history_list_display = ["changed_fields", "list_changes"]

    def changed_fields(self, obj):
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)
            return ", ".join(delta.changed_fields)
        return "Criação Inicial"
    changed_fields.short_description = 'Campos Alterados'