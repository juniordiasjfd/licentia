from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied

class LicentiaPermissionMixin(UserPassesTestMixin):
    """Classe base para padronizar o erro 403 em todos os mixins"""
    def handle_no_permission(self):
        raise PermissionDenied

class CoordenadorRequiredMixin(LicentiaPermissionMixin):
    def test_func(self):
        user = self.request.user
        return user.is_superuser or user.groups.filter(name='Coordenador').exists()

class ComumInternoRequiredMixin(LicentiaPermissionMixin):
    def test_func(self):
        user = self.request.user
        grupos_autorizados = ['Coordenador', 'Comum interno']
        return user.is_superuser or user.groups.filter(name__in=grupos_autorizados).exists()

class ComumExternoRequiredMixin(LicentiaPermissionMixin):
    def test_func(self):
        user = self.request.user
        grupos_autorizados = ['Coordenador', 'Comum interno', 'Comum externo']
        return user.is_superuser or user.groups.filter(name__in=grupos_autorizados).exists()