# licentia_process/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from .models import Process, ProcessLog
from .forms import ProcessForm
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect


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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['historico_alteracoes'] = []
        return context

class ProcessUpdateView(ProcessContextMixin, UpdateView):
    model = Process
    form_class = ProcessForm
    template_name = 'licentia_process/process_form.html'
    success_url = reverse_lazy('process:process_list')

    def form_valid(self, form):
        # Pega os usuários antes da alteração
        old_assignees = set(self.object.atribuido_a.all())

        response = super().form_valid(form)

        # Pega os usuários depois da alteração
        new_assignees = set(self.object.atribuido_a.all())

        if old_assignees != new_assignees:
            adicionados = [u.get_full_name() or u.username for u in (new_assignees - old_assignees)]
            removidos = [u.get_full_name() or u.username for u in (old_assignees - new_assignees)]
            
            msg = []
            if adicionados: msg.append(f"Atribuído a: {', '.join(adicionados)}")
            if removidos: msg.append(f"Removido de: {', '.join(removidos)}")
            
            # Cria um registro no Diário de Bordo automaticamente
            ProcessLog.objects.create(
                processo=self.object,
                usuario=self.request.user,
                texto=f"Alteração de atribuição: {'; '.join(msg)}"
            )

        form.instance.atualizado_por = self.request.user
        messages.success(self.request, f"Processo {self.object.retranca} atualizado!")
        # Se o botão "permanecer" foi clicado, redireciona para a mesma página
        if "_continue" in self.request.POST:
            return redirect('process:process_update', pk=self.object.pk)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        records = self.object.history.all().order_by('-history_date')
        CAMPOS_EXCLUIDOS = ["criado_por", "atualizado_por"]

        historico = []

        for record in records:
            if record.prev_record:
                delta = record.diff_against(record.prev_record)

                lista = []
                for change in delta.changes:
                     # ignora campos indesejados
                    if change.field in CAMPOS_EXCLUIDOS:
                        continue

                    try:
                        field = self.model._meta.get_field(change.field)
                        verbose = field.verbose_name
                    except Exception:
                        field = None
                        verbose = change.field

                    old_value = change.old
                    new_value = change.new

                    # ----------------------------
                    # Converter FK pk -> objeto
                    # ----------------------------
                    if field and field.is_relation and field.many_to_one:
                        model_fk = field.related_model

                        if old_value:
                            try:
                                old_value = model_fk.objects.get(pk=old_value)
                            except model_fk.DoesNotExist:
                                pass

                        if new_value:
                            try:
                                new_value = model_fk.objects.get(pk=new_value)
                            except model_fk.DoesNotExist:
                                pass

                    lista.append({
                        "field": change.field,
                        "verbose": verbose,
                        "old": old_value,
                        "new": new_value,
                    })

                record.lista_changes = lista
            else:
                record.lista_changes = []

            historico.append(record)

        context["historico_alteracoes"] = historico
        return context

class SaveProcessLogView(View):
    def post(self, request, *args, **kwargs):
        texto = request.POST.get('texto')
        processo_id = request.POST.get('processo_id')
        
        if texto and processo_id:
            processo = Process.objects.get(id=processo_id)
            log = ProcessLog.objects.create(
                processo=processo,
                usuario=request.user,
                texto=texto
            )
            return JsonResponse({
                'status': 'success',
                'usuario': log.usuario.get_full_name() or log.usuario.username,
                'data': log.data_criacao.strftime('%d/%m/%Y %H:%M'), 
                'texto': log.texto
            })
        return JsonResponse({'status': 'error'}, status=400)



