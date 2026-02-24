# licentia_process/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from .models import Process
from .forms import ProcessForm

class ProcessContextMixin:
    """Mixin para padronizar variáveis de template e URLs"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        context['model_name'] = self.model._meta.model_name
        context['url_listagem'] = reverse_lazy('process:process_list')
        return context

class ProcessListView(ProcessContextMixin, ListView):
    model = Process
    template_name = 'licentia_process/process_list.html'
    context_object_name = 'objetos'
    ordering = ['-data_entrada']

class ProcessCreateView(ProcessContextMixin, CreateView):
    model = Process
    form_class = ProcessForm
    template_name = 'licentia_process/process_form.html'
    success_url = reverse_lazy('process:process_list')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        messages.success(self.request, "Novo processo registrado com sucesso!")
        return super().form_valid(form)

class ProcessUpdateView(ProcessContextMixin, UpdateView):
    model = Process
    form_class = ProcessForm
    template_name = 'process/process_form.html'
    success_url = reverse_lazy('process:process_list')

    def form_valid(self, form):
        form.instance.atualizado_por = self.request.user
        messages.success(self.request, f"Processo {self.object.retranca} atualizado!")
        return super().form_valid(form)