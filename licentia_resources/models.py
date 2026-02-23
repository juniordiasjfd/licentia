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

class StatusDoOrcamento(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True, help_text='Situação de recebimento do orçamento.')
    class Meta:
        verbose_name = 'Status do orçamento'
        verbose_name_plural = 'Status dos orçamentos'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class StatusDoOrcamentoAprovacao(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True, help_text='Situação de aprovação do orçamento.')
    class Meta:
        verbose_name = 'Status de aprovação do orçamento'
        verbose_name_plural = 'Status de aprovações de orçamento'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class StatusDoProcessoPagamentoFornecedor(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True, help_text='Situação do pagamento.')
    class Meta:
        verbose_name = 'Status de pagamento do fornecedor'
        verbose_name_plural = 'Status de pagamentos dos fornecedores'
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

class StatusAnaliseEditorial(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Análise editorial'
        verbose_name_plural = 'Análises editoriais'
    def __str__(self):
        return self.nome

class StatusAnaliseAutRec(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Análise AutRec'
        verbose_name_plural = 'Análises AutRec'
    def __str__(self):
        return self.nome

class LocalizacaoDoRecurso(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Localização do recurso'
        verbose_name_plural = 'Localizações dos recursos'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class Fornecedor(AuditoriaBase):
    nome = models.CharField('Nome fantasia', max_length=200, unique=True, help_text='Nome fantasia ou autor')
    razao_social = models.CharField('Razão social', max_length=200, unique=True, help_text='Razão social')
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome']
    def __str__(self):
        return f'{self.nome} - {self.razao_social}'

class Empresa(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Empresa de faturamento'
        verbose_name_plural = 'Empresas de faturamento'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class CentroDeCusto(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Centro de custo'
        verbose_name_plural = 'Centros de custo'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class TipoDeTermo(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Tipo de termo'
        verbose_name_plural = 'Tipos de termo'
        ordering = ['nome']
    def __str__(self):
        return self.nome

class LimitacaoEdicao(AuditoriaBase):
    nome = models.CharField('Nome', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Limitação de edição'
        verbose_name_plural = 'Limitações de edição'
        ordering = ['nome']
    def __str__(self):
        return self.nome





