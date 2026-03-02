from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UsuarioAdmin(UserAdmin):
    # 1. Substituímos os campos ManyToMany por nomes de métodos
    list_display = (
        'username', 'first_name', 'last_name', 'email', 
        'is_staff', 'is_active', 'get_departamentos', 
    )
    
    filter_horizontal = ('groups', 'user_permissions')
    
    # 2. Adicionamos os campos personalizados aos fieldsets originais do Django
    # Isso garante que eles apareçam na tela de edição
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {'fields': ('departamentos', )}),
    )

    # 3. Método para exibir departamentos na lista
    def get_departamentos(self, obj):
        return ", ".join([d.nome for d in obj.departamentos.all()])
    get_departamentos.short_description = 'Departamentos'

    # 5. Otimização de performance (evita centenas de queries no banco)
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('departamentos')