from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from core.models import AuditoriaBase
from licentia_resources import models as resources_models
from users import models as users_models
from simple_history.models import HistoricalRecords


def get_default_status_orcamento_aprovacao():
    from licentia_resources.models import StatusDoOrcamentoAprovacao
    status = StatusDoOrcamentoAprovacao.objects.filter(nome__icontains='PEND').first()
    return status.id if status else None
def get_default_status_orcamento():
    from licentia_resources.models import StatusDoOrcamento
    status = StatusDoOrcamento.objects.filter(nome__icontains='PEND').first()
    return status.id if status else None
class Process(AuditoriaBase):
    volume = models.PositiveIntegerField('Volume', blank=True, null=True)
    pagina = models.PositiveIntegerField('Página', blank=True, null=True)
    unidade = models.PositiveIntegerField('Unidade', blank=True, null=True)
    lote = models.PositiveIntegerField('Lote', blank=True, null=True)
    limitacao_anos = models.PositiveIntegerField('Limitação (anos)', blank=True, null=True)
    limitacao_tiragem = models.PositiveIntegerField('Limitação (tiragem)', blank=True, null=True)

    valor_do_processo = models.DecimalField(
        'Valor (R$)', 
        max_digits=12, 
        decimal_places=2, 
        blank=True, 
        null=True
    )

    retranca = models.CharField('Retranca', max_length=100, unique=True)
    capitulo_secao = models.CharField('Capítulo ou seção', max_length=100, blank=True, null=True)
    titulo_descricao = models.CharField('Título ou descrição', max_length=200, blank=True, null=True)
    solicitado_para = models.CharField('Solicitado para', max_length=200, blank=True, null=True)
    
    obra_original = models.TextField('Obra original', max_length=1000, blank=True, null=True)
    codigo_biblioteca_link = models.TextField('Código da biblioteca ou link', max_length=1000, blank=True, null=True)
    observacao_exemplares = models.TextField('Observação exemplares', max_length=1000, blank=True, null=True)
    limitacao_outros = models.TextField('Limitação (outros)', max_length=1000, blank=True, null=True)
    
    observacao_editorial = CKEditor5Field("Observação editorial", config_name='default', blank=True, null=True)
    credito_obrigatorio = CKEditor5Field("Crédito obrigatório", config_name='default', blank=True, null=True)
    observacao_autrec = CKEditor5Field("Observação AutRec", config_name='default', blank=True, null=True)

    solicitar_imagem = models.BooleanField('Solicitar imagem', default=False)
    enviar_formulario = models.BooleanField('Enviar formulário', default=False)

    data_entrada = models.DateField('Data de entrada', null=True, blank=True)
    data_analise_autrec = models.DateField('Data de análise AutRec', null=True, blank=True)

    localizacao_do_recurso = models.ForeignKey(
        resources_models.LocalizacaoDoRecurso, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_localizacao",
        verbose_name="Localização do recurso")
    
    fornecedor = models.ForeignKey(
        resources_models.Fornecedor, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_fornecedor",
        verbose_name="Autor e fornecedor")
    
    status_analise_editorial = models.ForeignKey(
        resources_models.StatusAnaliseEditorial, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_analise_editorial",
        verbose_name="Status da análise editorial")

    status_analise_autrec = models.ForeignKey(
        resources_models.StatusAnaliseAutRec, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_analise_autrec",
        verbose_name="Status da análise AutRec")
    
    status_do_orcamento = models.ForeignKey(
        resources_models.StatusDoOrcamento, 
        on_delete=models.PROTECT,
        default=get_default_status_orcamento,
        null=True,
        blank=True,
        related_name="%(class)s_status_orcamento",
        verbose_name="Status do orçamento")
    
    status_do_orcamento_aprovacao = models.ForeignKey(
        resources_models.StatusDoOrcamentoAprovacao, 
        on_delete=models.PROTECT,
        default=get_default_status_orcamento_aprovacao,
        null=True,
        blank=True,
        related_name="%(class)s_status_orcamento_aprovacao",
        verbose_name="Status do orçamento aprovação")
    
    status_do_processo = models.ForeignKey(
        resources_models.StatusDoProcesso, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_status_do_processo",
        verbose_name="Status do processo")
    
    status_do_processo_pagamento_fornecedor = models.ForeignKey(
        resources_models.StatusDoProcessoPagamentoFornecedor, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_status_do_processo_pagamento_fornecedor",
        verbose_name="Pagamento para o fornecedor")
    
    empresa = models.ForeignKey(
        resources_models.Empresa, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_empresa",
        verbose_name="Empresa")
    
    centro_de_custo = models.ForeignKey(
        resources_models.CentroDeCusto, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_centro_de_custo",
        verbose_name="Centro de custo")
    
    tipo_de_termo = models.ForeignKey(
        resources_models.TipoDeTermo, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_tipo_de_termo",
        verbose_name="Termo")
    
    limitacao_edicao = models.ForeignKey(
        resources_models.LimitacaoEdicao, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_limitacao_edicao",
        verbose_name="Limitação (edições)")
    
    status_do_freela_pagamento = models.ForeignKey(
        resources_models.StatusDoFreelaPagamento, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_status_do_freela_pagamento",
        verbose_name="Status de pagamento do externo")
    
    projeto = models.ForeignKey(
        resources_models.Projeto, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_projeto",
        verbose_name="Projeto")
    
    componente = models.ForeignKey(
        resources_models.Componente, 
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(class)s_componente",
        verbose_name="Componente")

    atribuido_a = models.ManyToManyField(
        users_models.User, 
        blank=True,
        verbose_name="Atribuído a",
        related_name="%(class)s_atribuicoes",
        help_text='Marque os usuários atribuídos.')
    
    history = HistoricalRecords(custom_model_name='HistoricalProcess')

    @property
    def lista_mudancas(self):
        # Este método será usado no template
        return self.get_lista_mudancas()

    def get_lista_mudancas(self):
        # Lógica para ser usada via objeto de histórico ou objeto real
        if hasattr(self, 'prev_record') and self.prev_record:
            delta = self.diff_against(self.prev_record)
            # Retorna os nomes dos campos alterados
            return ", ".join(delta.changed_fields)
        return ""

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'
        ordering = ['-data_entrada', 'retranca']

    def __str__(self):
        return f"{self.retranca} - {self.titulo_descricao or 'Sem título'}"


