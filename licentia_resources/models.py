from django.db import models
from core.models import AuditoriaBase


class Componente(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Componente'
        verbose_name_plural = 'Componentes'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class Projeto(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    editora = models.CharField('Editora', max_length=100)
    ciclo = models.CharField('Ciclo', max_length=100)
    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class StatusDoProcesso(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Status do processo'
        verbose_name_plural = 'Status dos processos'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class StatusDoProcessoPagamento(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Status de pagamento do processo'
        verbose_name_plural = 'Status de pagamentos dos processos'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class StatusDoFreelaPagamento(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Status de pagamento do freela'
        verbose_name_plural = 'Status de pagamentos dos freelas'
        ordering = ['nome']
    def __str__(self):
        return self.nome
