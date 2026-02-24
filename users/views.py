from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from .forms import RegistroUsuarioForm, AtivacaoUsuarioForm, DepartamentoForm
from django.contrib import messages
from .models import User, Departamento
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CoordenadorRequiredMixin
from django.views import View


# Mixin para centralizar o contexto comum (DRY)
class DepartamentoContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.model._meta.verbose_name
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        context['model_name'] = self.model._meta.model_name
        context['url_listagem'] = reverse_lazy('users:departamento_list')
        return context

# View de Listagem
class DepartamentoListView(LoginRequiredMixin, DepartamentoContextMixin, ListView):
    model = Departamento
    template_name = 'users/users_list.html'
    context_object_name = 'objetos'

# View de Criação
class DepartamentoCreateView(CoordenadorRequiredMixin, DepartamentoContextMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = "users/users_form.html"
    success_url = reverse_lazy("users:departamento_list")

    def form_valid(self, form):
        # Opcional: Se quiser registrar auditoria aqui também
        form.instance.criado_por = self.request.user
        messages.success(self.request, f"{self.model._meta.verbose_name} criado com sucesso!")
        return super().form_valid(form)

# View de Edição
class DepartamentoUpdateView(CoordenadorRequiredMixin, DepartamentoContextMixin, UpdateView):
    model = Departamento # Corrigido: era DepartamentoForm
    form_class = DepartamentoForm
    template_name = "users/users_form.html"
    success_url = reverse_lazy("users:departamento_list")

    def form_valid(self, form):
        form.instance.atualizado_por = self.request.user
        messages.success(self.request, f"{self.model._meta.verbose_name} atualizado com sucesso!")
        return super().form_valid(form)

class RegistroView(CreateView):
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, 
            "Cadastro realizado! Sua conta está aguardando ativação por um coordenador."
        )
        return response

class GerenciarUsuariosView(CoordenadorRequiredMixin, ListView):
    model = User
    template_name = 'users/gerenciar_usuarios.html'
    context_object_name = 'usuarios'
    ordering = ['-date_joined']
    def get_queryset(self):
        # Exclui o próprio coordenador logado da lista para evitar auto-edição acidental
        return super().get_queryset().exclude(pk=self.request.user.pk).exclude(is_superuser=True)

class AtivarUsuarioView(CoordenadorRequiredMixin, View):
    def get(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        form = AtivacaoUsuarioForm(instance=usuario)
        return render(request, 'users/ativar_usuario_form.html', {
            'form': form, 
            'usuario_pendente': usuario
        })

    def post(self, request, pk):
        usuario = get_object_or_404(User, pk=pk)
        form = AtivacaoUsuarioForm(request.POST, instance=usuario)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Ativa o usuário
            user.save()
            
            form.save_m2m() 
            
            user.groups.clear()
            grupo_selecionado = form.cleaned_data['grupo']
            user.groups.add(grupo_selecionado)
            
            messages.success(request, f"Usuário {user.username} configurado e ativado!")
            return redirect('users:gerenciar')
            
        return render(request, 'users/ativar_usuario_form.html', {'form': form, 'usuario_pendente': usuario})

class SuspenderUsuarioView(CoordenadorRequiredMixin, View):
    """
    View para desativar o acesso de um usuário.
    Apenas acessível por Coordenadores ou Superusuários.
    """
    def post(self, request, pk):
        # Busca o usuário ou retorna 404
        usuario = get_object_or_404(User, pk=pk)
        
        # Impede que o coordenador suspenda a si próprio
        if usuario == request.user:
            messages.error(request, "Não podes suspender a tua própria conta.")
        else:
            usuario.is_active = False
            usuario.save()
            messages.success(request, f"O acesso de {usuario.username} foi suspenso com sucesso.")
        
        return redirect('users:gerenciar')

    def get(self, request, *args, **kwargs):
        # Redireciona para a lista se alguém tentar aceder via URL (GET)
        return redirect('users:gerenciar')




