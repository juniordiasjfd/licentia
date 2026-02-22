from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Mantemos apenas o que o Django não tem por padrão
    empresa = models.CharField("Empresa", max_length=100, null=True, blank=True)
    departamento = models.CharField("Departamento", max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"