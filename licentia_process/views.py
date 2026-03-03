# licentia_process/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from .models import Process, ProcessLog
from .forms import ProcessForm
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect
from django.db.models import Q
from .filters import ProcessFilter
from users.mixins import UsuarioComumRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User
import re
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.utils.html import escape
from django.shortcuts import get_object_or_404
from django.db import transaction
from core.models import Notification



class ProcessContextMixin(UsuarioComumRequiredMixin):
    login_url = 'users:login'
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
    # ordering = ['-atualizado_em']
    paginate_by = 100
    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            preferencia_ordem = self.request.user.configuracoes.ordenar_por
            queryset = queryset.order_by(preferencia_ordem)
        except:
            queryset = queryset.order_by('-atualizado_em')
        self.filterset = ProcessFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context
    # def get_paginate_by(self, queryset):
    #     return self.request.GET.get('paginate_by', self.paginate_by)
    def get_paginate_by(self, queryset):
        # Busca a config do usuário. Se não existir, usa o padrão 20.
        try:
            return self.request.user.configuracoes.registros_por_pagina
        except:
            return self.paginate_by

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

class BuscarUsuariosView(LoginRequiredMixin, View):
    def get(self, request):
        termo = request.GET.get("q", "")

        if not termo:
            return JsonResponse([], safe=False)

        usuarios = User.objects.filter(
                is_active=True
            ).filter(
                Q(username__icontains=termo) |
                Q(first_name__icontains=termo) |
                Q(last_name__icontains=termo)
            ).only("username", "first_name", "last_name", "email")[:10]

        resultados = [
            {
                "key": u.username,
                "value": u.get_full_name() or u.username,
                "email": u.email
            }
            for u in usuarios
        ]

        return JsonResponse(resultados, safe=False)

def extrair_mencoes(texto):
    """
    Retorna uma lista de usernames mencionados com @
    Ex: '@junior @maria' -> ['junior', 'maria']
    """
    padrao = r'@([\w.@+-]+)'
    return re.findall(padrao, texto)

def formatar_mencoes(texto):
    """
    Escapa o texto para evitar XSS
    e transforma @usuario em badge HTML.
    """
    texto_seguro = escape(texto)

    return re.sub(
        r'@([\w.@+-]+)',
        r'<span class="badge bg-teal">@\1</span>',
        texto_seguro
    )

class SaveProcessLogView(View):

    def post(self, request, *args, **kwargs):

        texto = request.POST.get('texto')
        processo_id = request.POST.get('processo_id')

        if not texto or not processo_id:
            return JsonResponse({'status': 'error'}, status=400)

        # Busca segura do processo
        processo = get_object_or_404(Process, id=processo_id)

        with transaction.atomic():

            # Cria o log uma única vez
            log = ProcessLog.objects.create(
                processo=processo,
                usuario=request.user,
                texto=texto
            )

            # Gera URL absoluta
            url_relativa = reverse('process:process_update', kwargs={'pk': processo.pk})
            url_absoluta = request.build_absolute_uri(url_relativa)

            # Detecta menções
            usernames_mencionados = set(extrair_mencoes(texto))

            for username in usernames_mencionados:

                try:
                    user_mencionado = User.objects.get(username=username)

                    # # Não envia para si mesmo
                    # if user_mencionado == request.user:
                    #     continue
                    Notification.objects.create(
                        usuario=user_mencionado,
                        processo=processo,
                        log=log,
                        mensagem=f"Você foi mencionado no processo {processo.retranca} [{texto}]",
                        url=url_relativa
                    )

                    config = getattr(user_mencionado, "configuracoes", None)

                    if (
                        user_mencionado.is_active and
                        user_mencionado.email and
                        config and
                        config.receber_notificacoes_email
                    ):

                        send_mail(
                            subject=f"Você foi mencionado no processo {processo.retranca}",
                            message=f"""
Olá {user_mencionado.get_full_name() or user_mencionado.username},

Você foi mencionado no diário de bordo do processo: {processo.retranca}

Mensagem:
"{texto}"

Autor da mensagem: {request.user.get_full_name() or request.user.username}

Acesse diretamente pelo link: {url_absoluta}

---
Sistema Licentia
""",
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[user_mencionado.email],
                            fail_silently=True,
                        )

                except User.DoesNotExist:
                    continue

        return JsonResponse({
            'status': 'success',
            'usuario': log.usuario.get_full_name() or log.usuario.username,
            'data': log.data_criacao.strftime('%d/%m/%Y %H:%M'),
            'texto': formatar_mencoes(log.texto)
        })





