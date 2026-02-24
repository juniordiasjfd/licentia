from django import forms
from .models import Process

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        exclude = ('criado_por', 'atualizado_por', 'criado_em', 'atualizado_em')
        widgets = {
            'retranca': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_do_processo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'data_entrada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_analise_autrec': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # Adicione classes form-select para todas as ForeignKeys
            'projeto': forms.Select(attrs={'class': 'form-select'}),
            'status_do_processo': forms.Select(attrs={'class': 'form-select'}),
            'atribuido_a': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }