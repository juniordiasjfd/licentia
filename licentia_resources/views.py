from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from . import models as resources_models
from .forms import BaseResourceForm
from django import forms
from collections import OrderedDict


class ResourceContextMixin:
    """Mixin para centralizar os dados comuns de contexto para as views de Recursos."""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Dados para o template saber qual modelo está manipulando
        context['verbose_name'] = self.model._meta.verbose_name
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        context['model_name'] = self.model._meta.model_name
        # URL de cancelamento dinâmica
        context['url_listagem'] = reverse_lazy(f'resources:{self.model._meta.model_name}_list')
        return context
class ResourceBaseCreateUpdateView(ResourceContextMixin):
    template_name = 'licentia_resources/resource_form.html'
    # form_class = BaseResourceForm # Usa o form base com estilo Tabler

    def get_form_class(self):
        # Cria um ModelForm dinâmico baseado no modelo da View
        return type('DynamicForm', (BaseResourceForm,), {'Meta': type('Meta', (), {'model': self.model, 'fields': '__all__'})}) # , 'exclude': ['criado_por', 'atualizado_por']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # 1. Definimos os campos de auditoria
        audit_fields = ['criado_por', 'atualizado_por', 'criado_em', 'atualizado_em']
        
        # 2. Tenta pegar o objeto atual (se for UpdateView ele existe, se for CreateView é None)
        obj = getattr(self, 'object', None)
        
        # 3. Adicionamos as datas manualmente APENAS se o objeto já existir (Edição)
        if obj and obj.pk:
            if 'criado_em' in audit_fields:
                form.fields['criado_em'] = forms.CharField(
                    label="Criado em",
                    initial=obj.criado_em.strftime('%d/%m/%Y %H:%M') if obj.criado_em else "",
                    disabled=True,
                    required=False,
                    widget=forms.TextInput(attrs={'class': 'form-control bg-light'})
                )
            if 'atualizado_em' in audit_fields:
                form.fields['atualizado_em'] = forms.CharField(
                    label="Atualizado em",
                    initial=obj.atualizado_em.strftime('%d/%m/%Y %H:%M') if obj.atualizado_em else "",
                    disabled=True,
                    required=False,
                    widget=forms.TextInput(attrs={'class': 'form-control bg-light'})
                )

        # 4. Reordenar campos (Auditoria por último)
        # Criamos uma lista com os campos que não são de auditoria primeiro
        new_order = [f for f in form.fields.keys() if f not in audit_fields]
        # Adicionamos os de auditoria que existem no form ao final
        new_order.extend([f for f in audit_fields if f in form.fields])
        
        from collections import OrderedDict
        form.fields = OrderedDict((k, form.fields[k]) for k in new_order)

        # 5. Bloquear campos de usuários
        for field_name in ['criado_por', 'atualizado_por']:
            if field_name in form.fields:
                form.fields[field_name].disabled = True
                form.fields[field_name].required = False

        return form
    
    def form_valid(self, form):
        if not form.instance.pk:
            form.instance.criado_por = self.request.user
        form.instance.atualizado_por = self.request.user
        if not self.object:
            messages.success(self.request, f"{self.model._meta.verbose_name} criado com sucesso!")
        else:
            messages.success(self.request, f"{self.model._meta.verbose_name} atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Dispara uma mensagem de erro para o pop-up global
        messages.error(self.request, "Erro ao salvar: verifique os campos abaixo.")
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy(f'resources:{self.model._meta.model_name}_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['model_name'] = self.model._meta.model_name
        # Gera a URL de listagem dinamicamente para o botão Cancelar
        context['url_listagem'] = reverse_lazy(f'resources:{self.model._meta.model_name}_list')
        return context
class ResourceBaseListView(ResourceContextMixin, ListView):
    template_name = 'licentia_resources/resource_list.html'
    context_object_name = 'objetos'

# --- COMPONENTE ---
class ComponenteListView(ResourceBaseListView):
    model = resources_models.Componente
class ComponenteCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.Componente
class ComponenteUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.Componente

# --- PROJETO ---
class ProjetoListView(ResourceBaseListView):
    model = resources_models.Projeto
class ProjetoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.Projeto
class ProjetoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.Projeto

# --- STATUSDOPROCESSO ---
class StatusDoProcessoListView(ResourceBaseListView):
    model = resources_models.StatusDoProcesso
class StatusDoProcessoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.StatusDoProcesso
class StatusDoProcessoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.StatusDoProcesso

# --- StatusDoOrcamento ---
class StatusDoOrcamentoListView(ResourceBaseListView):
    model = resources_models.StatusDoOrcamento
class StatusDoOrcamentoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.StatusDoOrcamento
class StatusDoOrcamentoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.StatusDoOrcamento

# --- StatusDoOrcamentoAprovacao ---
class StatusDoOrcamentoAprovacaoListView(ResourceBaseListView):
    model = resources_models.StatusDoOrcamentoAprovacao
class StatusDoOrcamentoAprovacaoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.StatusDoOrcamentoAprovacao
class StatusDoOrcamentoAprovacaoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.StatusDoOrcamentoAprovacao

# --- StatusDoProcessoPagamentoFornecedor ---
class StatusDoProcessoPagamentoFornecedorListView(ResourceBaseListView):
    model = resources_models.StatusDoProcessoPagamentoFornecedor
class StatusDoProcessoPagamentoFornecedorCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.StatusDoProcessoPagamentoFornecedor
class StatusDoProcessoPagamentoFornecedorUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.StatusDoProcessoPagamentoFornecedor

# --- StatusDoFreelaPagamento ---
class StatusDoFreelaPagamentoListView(ResourceBaseListView):
    model = resources_models.StatusDoFreelaPagamento
class StatusDoFreelaPagamentoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.StatusDoFreelaPagamento
class StatusDoFreelaPagamentoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.StatusDoFreelaPagamento

# --- StatusAnaliseEditorial ---
class StatusAnaliseEditorialListView(ResourceBaseListView):
    model = resources_models.StatusAnaliseEditorial
class StatusAnaliseEditorialCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.StatusAnaliseEditorial
class StatusAnaliseEditorialUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.StatusAnaliseEditorial

# --- StatusAnaliseAutRec ---
class StatusAnaliseAutRecListView(ResourceBaseListView):
    model = resources_models.StatusAnaliseAutRec
class StatusAnaliseAutRecCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.StatusAnaliseAutRec
class StatusAnaliseAutRecUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.StatusAnaliseAutRec

# --- LocalizacaoDoRecurso ---
class LocalizacaoDoRecursoListView(ResourceBaseListView):
    model = resources_models.LocalizacaoDoRecurso
class LocalizacaoDoRecursoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.LocalizacaoDoRecurso
class LocalizacaoDoRecursoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.LocalizacaoDoRecurso

# --- Fornecedor ---
class FornecedorListView(ResourceBaseListView):
    model = resources_models.Fornecedor
class FornecedorCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.Fornecedor
class FornecedorUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.Fornecedor

# --- Empresa ---
class EmpresaListView(ResourceBaseListView):
    model = resources_models.Empresa
class EmpresaCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.Empresa
class EmpresaUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.Empresa

# --- CentroDeCusto ---
class CentroDeCustoListView(ResourceBaseListView):
    model = resources_models.CentroDeCusto
class CentroDeCustoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.CentroDeCusto
class CentroDeCustoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.CentroDeCusto

# --- TipoDeTermo ---
class TipoDeTermoListView(ResourceBaseListView):
    model = resources_models.TipoDeTermo
class TipoDeTermoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.TipoDeTermo
class TipoDeTermoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.TipoDeTermo

# --- LimitacaoEdicao ---
class LimitacaoEdicaoListView(ResourceBaseListView):
    model = resources_models.LimitacaoEdicao
class LimitacaoEdicaoCreateView(ResourceBaseCreateUpdateView, CreateView):
    model = resources_models.LimitacaoEdicao
class LimitacaoEdicaoUpdateView(ResourceBaseCreateUpdateView, UpdateView):
    model = resources_models.LimitacaoEdicao


