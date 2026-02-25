from django import forms
from .models import Process


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        exclude = ('criado_por', 'atualizado_por', 'criado_em', 'atualizado_em')
        widgets = {
            'retranca': forms.TextInput(attrs={'class': 'form-control'}),
            'capitulo_secao': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_descricao': forms.TextInput(attrs={'class': 'form-control'}),

            'projeto': forms.Select(attrs={'class': 'form-select tom-select'}),
            'componente': forms.Select(attrs={'class': 'form-select tom-select'}),
            'localizacao_do_recurso': forms.Select(attrs={'class': 'form-select tom-select'}),
            'fornecedor': forms.Select(attrs={'class': 'form-select tom-select'}),
            'empresa': forms.Select(attrs={'class': 'form-select tom-select'}),
            'status_do_processo': forms.Select(attrs={'class': 'form-select tom-select'}),
            'status_analise_editorial': forms.Select(attrs={'class': 'form-select tom-select'}),
            'status_analise_autrec': forms.Select(attrs={'class': 'form-select tom-select'}),
            'status_do_orcamento': forms.Select(attrs={'class': 'form-select tom-select'}),
            'status_do_orcamento_aprovacao': forms.Select(attrs={'class': 'form-select tom-select'}),
            'tipo_de_termo': forms.Select(attrs={'class': 'form-select tom-select'}),
            'centro_de_custo': forms.Select(attrs={'class': 'form-select tom-select'}),
            'limitacao_edicao': forms.Select(attrs={'class': 'form-select tom-select'}),
            'status_do_freela_pagamento': forms.Select(attrs={'class': 'form-select tom-select'}),


            'volume': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'unidade': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'pagina': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'lote': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'limitacao_anos': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'limitacao_tiragem': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'valor_do_processo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),

            'obra_original': forms.Textarea(attrs={'class': 'form-control'}),
            'codigo_biblioteca_link': forms.Textarea(attrs={'class': 'form-control'}),
            'observacao_exemplares': forms.Textarea(attrs={'class': 'form-control'}),
            'limitacao_outros': forms.Textarea(attrs={'class': 'form-control'}),

            'solicitar_imagem': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch'}),
            'enviar_formulario': forms.CheckboxInput(attrs={'class': 'form-check-input', 'role': 'switch'}),
            
            
            'data_entrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_analise_autrec': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            # Adicione classes form-select para todas as ForeignKeys
            'atribuido_a': forms.SelectMultiple(attrs={
                'class': 'form-select tom-select', 
                'placeholder': 'Selecione os responsáveis...'
            }),
        }