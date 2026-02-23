from django.db import models
from django.conf import settings

class AuditoriaBase(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    # Usamos settings.AUTH_USER_MODEL para referenciar seu modelo de usuário customizado
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_criados",
        verbose_name="Criador por"
    )
    atualizado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_atualizados",
        verbose_name="Atualizado por"
    )

    class Meta:
        abstract = True