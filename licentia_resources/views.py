from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Componente, Projeto, StatusDoProcesso, StatusDoProcessoPagamento, StatusDoFreelaPagamento
from .forms import BaseResourceForm


class ResourceBaseView:
    template_name = 'licentia_resources/resource_form.html'
    form_class = BaseResourceForm # Usa o form base com estilo Tabler

    def get_form_class(self):
        # Cria um ModelForm dinâmico baseado no modelo da View
        return type('DynamicForm', (BaseResourceForm,), {'Meta': type('Meta', (), {'model': self.model, 'fields': '__all__', 'exclude': ['criado_por', 'atualizado_por']})})

    def form_valid(self, form):
        if not form.instance.pk:
            form.instance.criado_por = self.request.user
        form.instance.atualizado_por = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(f'resources:{self.model._meta.model_name}_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['model_name'] = self.model._meta.model_name
        
        # Gera a URL de listagem dinamicamente para o botão Cancelar
        context['url_listagem'] = reverse_lazy(f'resources:{self.model._meta.model_name}_list')
        
        return context

# --- COMPONENTE ---
class ComponenteListView(ListView):
    model = Componente
    template_name = 'licentia_resources/resource_list.html'
    context_object_name = 'objetos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        context['model_name'] = self.model._meta.model_name
        return context
class ComponenteCreateView(ResourceBaseView, CreateView):
    model = Componente
class ComponenteUpdateView(ResourceBaseView, UpdateView):
    model = Componente

# --- PROJETO ---
class ProjetoListView(ListView):
    model = Projeto
    template_name = 'licentia_resources/resource_list.html'
    context_object_name = 'objetos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        context['model_name'] = self.model._meta.model_name
        return context
class ProjetoCreateView(ResourceBaseView, CreateView):
    model = Projeto
class ProjetoUpdateView(ResourceBaseView, UpdateView):
    model = Projeto

# --- STATUSDOPROCESSO ---
class StatusDoProcessoListView(ListView):
    model = StatusDoProcesso
    template_name = 'licentia_resources/resource_list.html'
    context_object_name = 'objetos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        context['model_name'] = self.model._meta.model_name
        return context
class StatusDoProcessoCreateView(ResourceBaseView, CreateView):
    model = StatusDoProcesso
class StatusDoProcessoUpdateView(ResourceBaseView, UpdateView):
    model = StatusDoProcesso





