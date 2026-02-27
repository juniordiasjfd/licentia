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

class ConfiguracoesDoUsuario(models.Model):
    registros_por_pagina = models.PositiveIntegerField('Número de processos por página', default=100)
    class OrdenarPorChoices(models.TextChoices):
        # Valor a ser salvo no DB, Display Name na interface
        ATUALIZADO_EM_ZA = '-atualizado_em', 'Atualizado em (Z-A)'
        ATUALIZADO_EM_AZ = 'atualizado_em', 'Atualizado em (A-Z)'
        RETRANCA_ZA = '-retranca', 'Retranca (Z-A)'
        RETRANCA_AZ = 'retranca', 'Retranca (A-Z)'
        STATUS_DO_PROCESSO_ZA = '-status_do_processo__nome', 'Status (Z-A)'
        STATUS_DO_PROCESSO_AZ = 'status_do_processo__nome', 'Status (A-Z)'
    ordenar_por = models.CharField(
        verbose_name='Ordenar lista de processos por',
        max_length=50,
        choices=OrdenarPorChoices.choices,
        default=OrdenarPorChoices.ATUALIZADO_EM_ZA,
    )
    usuario = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='configuracoes')
    class Meta:
        verbose_name = 'Configuração do usuário'