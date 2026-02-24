from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import AuditoriaBase

class Departamento(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class User(AbstractUser):
    departamentos = models.ManyToManyField(
        Departamento,
        blank=True,
        verbose_name="Departamentos",
        related_name="usuarios", # Adicionado para facilitar consultas inversas
        help_text='Marque os departamentos aos quais o usuário pertence.'
    )
    empresa = models.CharField("Empresa", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        # Como alteramos o __str__ antes, aqui está mantido conforme sua escolha
        return self.username