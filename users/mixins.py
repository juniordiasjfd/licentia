from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


class LicentiaPermissionMixin(UserPassesTestMixin):
    """Classe base para padronizar o erro 403 em todos os mixins"""
    def handle_no_permission(self):
        return redirect('users:login')
        # raise PermissionDenied

class CoordenadorRequiredMixin(LicentiaPermissionMixin):
    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.groups.filter(name='Coordenador').exists()

class UsuarioDoNucleoRequiredMixin(LicentiaPermissionMixin):
    def test_func(self):
        user = self.request.user
        grupos_autorizados = ['Coordenador', 'Usuário do núcleo']
        return user.is_superuser or user.groups.filter(name__in=grupos_autorizados).exists()

class UsuarioComumRequiredMixin(LicentiaPermissionMixin):
    def test_func(self):
        user = self.request.user
        grupos_autorizados = ['Coordenador', 'Usuário do núcleo', 'Usuário comum']
        return user.is_superuser or user.groups.filter(name__in=grupos_autorizados).exists()