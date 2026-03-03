

def notificacoes_context(request):
    if request.user.is_authenticated:
        return {
            "notificacoes_nao_lidas": request.user.notificacoes.filter(lida=False).count()
        }
    return {}