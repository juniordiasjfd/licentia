from django.apps import AppConfig
from django.db.models.signals import post_migrate


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

def create_user_groups(sender, **kwargs):
    from django.contrib.auth.models import Group
    groups = ['Coordenador', 'Usuário do núcleo', 'Usuário comum']
    for name in groups:
        Group.objects.get_or_create(name=name)

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        post_migrate.connect(create_user_groups, sender=self)