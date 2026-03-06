import django_filters
from django.db.models import Q
from .models import Process
from django import forms

class ProcessFilter(django_filters.FilterSet):
    # q = django_filters.CharFilter(method='filter_global_search', label="Busca geral")

    # Filtros de Data por Período (Mais útil que data exata)
    data_entrada_inicio = django_filters.DateFilter(
        field_name='data_entrada',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control form-control-sm"
        })
    )

    data_entrada_fim = django_filters.DateFilter(
        field_name='data_entrada',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control form-control-sm"
        })
    )

    data_analise_autrec_inicio = django_filters.DateFilter(
        field_name='data_analise_autrec',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control form-control-sm"
        })
    )

    data_analise_autrec_fim = django_filters.DateFilter(
        field_name='data_analise_autrec',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control form-control-sm"
        })
    )

    class Meta:
        model = Process
        fields = [
            'volume', 
            'unidade', 
            'lote', 
            'limitacao_anos', 
            'limitacao_tiragem',
            'solicitado_para',
            'localizacao_do_recurso',
            'status_analise_editorial',
            'status_analise_autrec',
            'status_do_orcamento',
            'status_do_orcamento_aprovacao',
            'status_do_processo',
            'status_do_processo_pagamento_fornecedor',
            'empresa',
            'centro_de_custo',
            'tipo_de_termo',
            'limitacao_edicao',
            'status_do_freela_pagamento',
            'projeto',
            'componente',
            'atribuido_a'
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.form.fields.items():

            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    "class": "form-select form-select-sm tom-select"
                })

            elif isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs.update({
                    "class": "form-select form-select-sm tom-select"
                })

            elif isinstance(field.widget, forms.DateInput):
                pass

            else:
                field.widget.attrs.update({
                    "class": "form-control form-control-sm"
                })
        
    # def filter_global_search(self, queryset, name, query):
    #     """
    #     Replica a lógica de busca em múltiplos campos que tínhamos na View.
    #     """
    #     return queryset.filter(
    #             # Q(volume__icontains=query) |
    #             Q(pagina__icontains=query) |
    #             # Q(unidade__icontains=query) |
    #             # Q(lote__icontains=query) |
    #             # Q(limitacao_anos__icontains=query) |
    #             # Q(limitacao_tiragem__icontains=query) |
    #             Q(retranca__icontains=query) |
    #             Q(capitulo_secao__icontains=query) |
    #             Q(titulo_descricao__icontains=query) |
    #             # Q(solicitado_para__icontains=query) |
    #             Q(obra_original__icontains=query) |
    #             Q(codigo_biblioteca_link__icontains=query) |
    #             Q(observacao_exemplares__icontains=query) |
    #             Q(limitacao_outros__icontains=query) |
    #             Q(observacao_editorial__icontains=query) |
    #             Q(credito_obrigatorio__icontains=query) |
    #             Q(observacao_autrec__icontains=query) |
    #             # Q(localizacao_do_recurso__nome__icontains=query) |
    #             Q(fornecedor__nome__icontains=query) |
    #             Q(fornecedor__razao_social__icontains=query) |
    #             # Q(status_analise_editorial__nome__icontains=query) |
    #             # Q(status_analise_autrec__nome__icontains=query) |
    #             # Q(status_do_orcamento__nome__icontains=query) |
    #             # Q(status_do_orcamento_aprovacao__nome__icontains=query) |
    #             # Q(status_do_processo__nome__icontains=query) |
    #             # Q(status_do_processo_pagamento_fornecedor__nome__icontains=query) |
    #             # Q(empresa__nome__icontains=query) |
    #             # Q(centro_de_custo__nome__icontains=query) |
    #             # Q(tipo_de_termo__nome__icontains=query) |
    #             # Q(limitacao_edicao__nome__icontains=query) |
    #             # Q(status_do_freela_pagamento__nome__icontains=query) |
    #             # Q(projeto__nome__icontains=query) |
    #             # Q(componente__nome__icontains=query) |
    #             # Q(atribuido_a__username__icontains=query) |
    #             # Q(atribuido_a__first_name__icontains=query) |
    #             # Q(atribuido_a__last_name__icontains=query) |
    #             Q(logs__texto__icontains=query)
    #         ).distinct()